from django import forms
from .models import Shtraf, Spisanie
from users.models import Otdel
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from dal import autocomplete

User = get_user_model()

class ShtrafForm(forms.ModelForm):
    class Meta:
        model = Shtraf
        fields = ['summa', 'reason']

# class DeductFineForm(forms.Form):
#     amount = forms.IntegerField(label='Списать сумму')

class FilterShtrafForm(forms.Form):
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    otdel = forms.ModelChoiceField(queryset=Otdel.objects.all(), required=False, empty_label="Все отделения")

class DeductFineForm(forms.ModelForm):
    class Meta:
        model = Spisanie
        fields = ['summa']
        labels = {
            'summa': 'Сумма списания',
        }

class FilterSpisanieForm(forms.Form):
    start_date = forms.DateField(label='Начало', required=False, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    end_date = forms.DateField(label='Конец', required=False, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    otdel = forms.ModelChoiceField(queryset=Otdel.objects.all(), required=False, empty_label="Все отделения")