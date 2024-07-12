"""
URL configuration for dolg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from shtraf.views import login_view, logout_view
from users.views import registration_view, CustomPasswordResetView


urlpatterns = [
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout' ),
    path('login/', login_view, name='login' ),
    path('password-reset/', CustomPasswordResetView.as_view(), name='custom_password_reset'),

    # URL для страницы "Сброс пароля - Успешно отправлено"
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/custom_reset_done.html'), name='password_reset_done'),

    # URL для страницы подтверждения сброса пароля (reset/<uidb64>/<token>/)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),

    # URL для страницы успешного завершения сброса пароля
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('', include('shtraf.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    print(f"Serving media files from {settings.MEDIA_URL} at {settings.MEDIA_ROOT}")
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)