from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from django.conf import settings  
from django.conf.urls.static import static  
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', core_views.home, name='home'),
    path('update/<int:uid>',core_views.update,name='update'),
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 
