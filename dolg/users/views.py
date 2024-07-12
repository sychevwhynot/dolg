from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import RegistrationForm, CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy


User = get_user_model()

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу успешной регистрации или другую страницу
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'  # Используем ваш кастомный шаблон
    email_template_name = 'registration/password_reset_email.html'  # Шаблон email для отправки ссылки сброса пароля
    success_url = reverse_lazy('password_reset_done')