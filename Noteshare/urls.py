from django.contrib import admin
from django.urls import path, include
from users.views import home,about_view,contact_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from notes.views import debug_media


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('notes/', include('notes.urls')),
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'), 
    path('about/', about_view, name='about'), 
    path('debug-media/', debug_media, name='debug_media'),
]
    
urlpatterns +=[
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
]