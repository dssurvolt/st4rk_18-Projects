from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student
from .models import Module, Grade, Notification, Message
from django.contrib import messages as flash_messages
from .models import UserProfile

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
    modules = student.modules.all()
    grades = Grade.objects.filter(student=student)
    notifications = student.notifications.filter(is_read=False).order_by('-created_at')
    messages = request.user.received_messages.order_by('-sent_at')[:5]

    return render(request, 'core/dashboard.html', {
        'modules': modules,
        'grades': grades,
        'notifications': notifications,
        'messages': messages,
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
