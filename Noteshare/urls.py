from django.contrib import admin
from django.urls import path, include
from users.views import home,about_view,contact_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('notes/', include('notes.urls')),
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'), 
    path('about/', about_view, name='about'), 
]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)