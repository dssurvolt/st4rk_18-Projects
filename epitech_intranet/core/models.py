from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Student(AbstractUser):
    promo = models.CharField(max_length=10)
    github = models.URLField(blank=True, null=True)
    epitech_email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    grade = models.FloatField()

    def __str__(self):
        return f"{self.student} - {self.module} : {self.grade}"
    
class Notification(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notifications')
    content = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.student.username} - {self.content[:20]}..."

class Message(models.Model):
    sender = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.sender} -> {self.recipient} : {self.content[:30]}"

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('etudiant', 'Étudiant'),
        ('admin', 'Admin'),
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='etudiant')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"