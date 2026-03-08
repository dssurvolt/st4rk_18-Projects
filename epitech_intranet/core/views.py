from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student
from .models import Module, Grade, Notification, Message
from django.contrib import messages as flash_messages
from .models import UserProfile
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404

def home(request):
    if request.user.is_authenticated:
        return render(request, 'core/home.html', {'student': request.user})
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    student = request.user
    grades = Grade.objects.filter(student=student).select_related('module', 'student')
    notifications = student.notifications.filter(is_read=False).order_by('-created_at')
    messages = request.user.received_messages.select_related('sender', 'recipient').order_by('-sent_at')[:5]
    
    # Cache la liste des étudiants pour éviter requêtes répétées
    students = cache.get('students_list')
    if students is None:
        students = list(Student.objects.exclude(id=student.id).values('id', 'username', 'first_name', 'last_name'))
        cache.set('students_list', students, 60*15)  # Cache 15 min
    
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        content = request.POST.get('content')
        if recipient_username and content:
            try:
                recipient = Student.objects.get(username=recipient_username)
                message = Message.objects.create(sender=request.user, recipient=recipient, content=content)
                flash_messages.success(request, f"Message envoyé à {recipient_username}")
                # Invalider cache si nécessaire
                cache.delete('students_list')
                
                # Envoyer notification email
                if recipient.epitech_email:
                    send_mail(
                        subject=f'Nouveau message de {request.user.first_name} {request.user.last_name}',
                        message=f'Vous avez reçu un nouveau message de {request.user.first_name} {request.user.last_name}:\n\n{content}\n\nConnectez-vous pour le lire.',
                        from_email=None,  # Utilise DEFAULT_FROM_EMAIL
                        recipient_list=[recipient.epitech_email],
                        fail_silently=True,
                    )
            except Student.DoesNotExist:
                flash_messages.error(request, "Destinataire introuvable.")
        else:
            flash_messages.error(request, "Champs requis manquants.")
        return redirect('dashboard')

    return render(request, 'core/dashboard.html', {
        'grades': grades,
        'notifications': notifications,
        'messages': messages,
        'students': students,
    })

def send_message(request):
    if request.method == 'POST':
        recipient_username = request.POST['recipient']
        content = request.POST['content']
        try:
            recipient = Student.objects.get(username=recipient_username)
            Message.objects.create(sender=request.user, recipient=recipient, content=content)
            flash_messages.success(request, f"Message envoyé à {recipient_username}")
        except Student.DoesNotExist:
            flash_messages.error(request, "Destinataire introuvable.")
        return redirect('dashboard')
    return render(request, 'core/send_message.html')

@login_required
def user_profile(request):
    profile = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'core/profile.html', {'profile': profile})

@login_required
def messages_view(request):
    messages_list = request.user.received_messages.select_related('sender').order_by('-sent_at')
    paginator = Paginator(messages_list, 10)  # 10 par page
    page_number = request.GET.get('page')
    messages = paginator.get_page(page_number)
    return render(request, 'core/messages.html', {'messages': messages})

@login_required
def chat_view(request, recipient_id):
    recipient = get_object_or_404(Student, id=recipient_id)
    if recipient == request.user:
        return redirect('dashboard')
    
    # Get messages between them
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('sent_at')
    
    room_name = f"{min(request.user.id, recipient.id)}_{max(request.user.id, recipient.id)}"
    
    return render(request, 'core/chat.html', {
        'recipient': recipient,
        'messages': messages,
        'room_name': room_name,
    })
