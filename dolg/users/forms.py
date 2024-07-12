from django import forms
from django.contrib.auth import get_user_model
from .models import Otdel
from django.contrib.auth.forms import PasswordResetForm

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Логин', max_length=50)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Имя', max_length=50, required=False)
    last_name = forms.CharField(label='Фамилия', max_length=50, required=False)
    superlast_name = forms.CharField(label='Отчество', max_length=50, required=False)
    otdel = forms.ModelChoiceField(label='Отделение', queryset=Otdel.objects.all(), empty_label='Выберите отделение', required=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'first_name', 'last_name', 'superlast_name', 'otdel']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Хешируем пароль
        if commit:
            user.save()
        return user
    
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        # Дополнительные проверки по вашему усмотрению
        return email