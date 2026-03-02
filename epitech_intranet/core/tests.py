from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
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

class APITest(APITestCase):
    def setUp(self):
        self.user = Student.objects.create_user(
            username='apiuser',
            password='testpass123',
            first_name='API',
            last_name='User'
        )

    def test_login_api(self):
        response = self.client.post('/api/login/', {
            'username': 'apiuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_dashboard_api_unauthenticated(self):
        response = self.client.get('/api/dashboard/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_dashboard_api_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/dashboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('modules', response.data)
