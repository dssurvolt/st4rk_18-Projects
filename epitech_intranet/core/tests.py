from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.cache import cache
from unittest.mock import patch
from .models import Student, Module, Grade, Message, Notification, UserProfile

User = get_user_model()

class StudentModelTest(TestCase):
    def test_student_creation(self):
        student = Student.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='test@example.com',
            promo='2025',
            github='https://github.com/test',
            epitech_email='test@epitech.eu'
        )
        self.assertEqual(student.username, 'testuser')
        self.assertEqual(str(student), 'Test User (testuser)')

class ModuleModelTest(TestCase):
    def test_module_creation(self):
        module = Module.objects.create(name='Python', description='Intro to Python')
        self.assertEqual(module.name, 'Python')
        self.assertEqual(str(module), 'Python')

class GradeModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create_user(username='student', password='pass')
        self.module = Module.objects.create(name='Math', description='Mathematics')

    def test_grade_creation(self):
        grade = Grade.objects.create(student=self.student, module=self.module, grade=15.5)
        self.assertEqual(grade.grade, 15.5)
        self.assertEqual(str(grade), f"{self.student} - {self.module} : 15.5")

class NotificationModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create_user(username='student', password='pass')

    def test_notification_creation(self):
        notification = Notification.objects.create(
            student=self.student,
            content='Nouvelle notification',
            is_read=False
        )
        self.assertEqual(notification.content, 'Nouvelle notification')
        self.assertFalse(notification.is_read)
        self.assertEqual(str(notification), f"{self.student.username} - Nouvelle notification...")

class MessageModelTest(TestCase):
    def setUp(self):
        self.sender = Student.objects.create_user(username='sender', password='pass')
        self.recipient = Student.objects.create_user(username='recipient', password='pass')

    def test_message_creation(self):
        message = Message.objects.create(
            sender=self.sender,
            recipient=self.recipient,
            content='Hello world'
        )
        self.assertEqual(message.content, 'Hello world')
        self.assertEqual(str(message), f"{self.sender} -> {self.recipient} : Hello world")

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create_user(username='student', password='pass')

    def test_user_profile_creation(self):
        profile = UserProfile.objects.create(user=self.student, role='etudiant')
        self.assertEqual(profile.role, 'etudiant')
        self.assertEqual(str(profile), 'student (etudiant)')

    @patch('PIL.Image.open')
    @patch('PIL.Image.thumbnail')
    def test_avatar_resizing(self, mock_thumbnail, mock_open):
        # Créer un avatar factice
        avatar = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        profile = UserProfile.objects.create(user=self.student, role='etudiant', avatar=avatar)
        # Le save devrait appeler resize_avatar
        profile.save()
        mock_open.assert_called()
        mock_thumbnail.assert_called_with((300, 300))

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Student.objects.create_user(
            username='testuser',
            password='password123',
            first_name='Test',
            last_name='User',
            epitech_email='test@epitech.eu'
        )

    def test_home_view_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Redirect to dashboard

    def test_home_view_unauthenticated(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/login.html')

    def test_login_view_post_success(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to home

    def test_login_view_post_failure(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid credentials')

    def test_dashboard_view_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/dashboard.html')

    def test_dashboard_view_unauthenticated(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    @patch('core.views.send_mail')
    def test_dashboard_send_message(self, mock_send_mail):
        self.client.login(username='testuser', password='password123')
        recipient = Student.objects.create_user(username='recipient', password='pass', epitech_email='rec@epitech.eu')
        
        response = self.client.post(reverse('dashboard'), {
            'recipient': 'recipient',
            'content': 'Test message'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Message.objects.filter(sender=self.user, recipient=recipient).exists())
        mock_send_mail.assert_called_once()

    def test_messages_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('messages'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/messages.html')

    def test_otp_setup_view_get(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('otp_setup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/otp_setup.html')

    @patch('django_otp.plugins.otp_totp.models.TOTPDevice.verify_token')
    def test_otp_setup_view_post_success(self, mock_verify):
        mock_verify.return_value = True
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('otp_setup'), {'otp_verify': '123456'})
        self.assertEqual(response.status_code, 302)  # Redirect to profile

    def test_search_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('search') + '?q=test')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/search.html')
