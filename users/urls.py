
from django.contrib import admin
from django.urls import path
from .views import home, signup , login_view, logout_view, about_view, contact_view, share_notes


urlpatterns = [
    path('',home, name='home'),
    path('register/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact"),
]
