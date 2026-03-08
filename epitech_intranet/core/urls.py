from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('send-message/', views.send_message, name='send_message'),
    path('messages/', views.messages_view, name='messages'),
    path('profile/', views.user_profile, name='profile'),
    path('chat/<int:recipient_id>/', views.chat_view, name='chat'),
]
