from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from land_registry.views import dashboard, web_properties, PropertyListAPI, PropertyDetailAPI, user_dashboard, web_register_user, web_login, web_property_detail, web_profile, web_password_reset
from consensus.views import web_validation, ValidationRequestAPI
from identity.ussd_views import web_ussd, USSDGateway
from identity.api_views import UserProfileAPI
from marketplace.views import ListingListAPI, web_marketplace
from config.swagger_views import swagger_ui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda r: redirect('web_login'), name='login_home'),
    # Espace Citoyen (Public & Personnel)
    path('login/', web_login, name='web_login'),
    path('password-reset/', web_password_reset, name='web_password_reset'),
    path('register/', web_register_user, name='web_register'),
    path('marketplace/', web_marketplace, name='web_marketplace'),
    path('dashboard/<str:wallet>/', user_dashboard, name='user_dashboard'),
    path('profile/<str:wallet>/', web_profile, name='web_profile'),
    path('property/<uuid:pk>/', web_property_detail, name='web_property_detail'),
    
    # Espace Supervision (Admin)
    path('supervision/', dashboard, name='dashboard'),
    path('supervision/properties/', web_properties, name='web_properties'),
    path('supervision/validation/', web_validation, name='web_validation'),
    path('supervision/ussd/', web_ussd, name='web_ussd'),
    
    # API Routes (REST)
    path('api/properties/', PropertyListAPI.as_view(), name='api_property_list'),
    path('api/properties/<uuid:pk>/', PropertyDetailAPI.as_view(), name='api_property_detail'),
    path('api/marketplace/listings/', ListingListAPI.as_view(), name='api_marketplace_list'),
    path('api/identity/profile/<str:wallet>/', UserProfileAPI.as_view(), name='api_user_profile'),
    
    # Consensus Flow
    path('api/validation/<str:action>/', ValidationRequestAPI.as_view(), name='api_validation_flow'),
    
    # USSD Gateway
    path('ussd/', USSDGateway.as_view(), name='ussd_gateway'),
    
    # Documentation
    path('swagger/', swagger_ui, name='swagger_ui'),
]
