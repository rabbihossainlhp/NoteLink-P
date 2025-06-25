from django.urls import path
from . import views

urlpatterns = [
    path('notes_feed/', views.note_home, name='note_home'),
    path('manage/', views.note_list, name='note_list'),
    path('edit/<int:note_id>/', views.note_edit, name='note_edit'),
    path('delete/<int:note_id>/', views.note_delete, name='note_delete'),
    path('', views.note_list, name='note_list'),
]
