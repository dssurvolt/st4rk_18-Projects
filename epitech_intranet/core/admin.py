from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student
from .models import Module, Grade
from .models import UserProfile

class StudentAdmin(UserAdmin):
    model = Student
    list_display = ('username', 'first_name', 'last_name', 'promo', 'epitech_email')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('promo', 'github', 'epitech_email')}),
    )

admin.site.register(Student, StudentAdmin)
admin.site.register(Module)
admin.site.register(Grade)
admin.site.register(UserProfile)