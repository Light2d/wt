from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, login, register, logout, sportgrounds, events, activate_account
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm

urlpatterns = [
    path('', index, name='index'),
    path('events', events, name='events'),
    path('sportgrounds', sportgrounds, name='sportgrounds'),
    
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'), 
    path('activate/<uuid:activation_code>/', activate_account, name='activate_account'),

   path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)