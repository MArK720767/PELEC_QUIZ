from django import forms
from django.contrib.auth.hashers import make_password

from .models import EventRegistration
from .validators import (
    normalize_full_name,
    normalize_gmail_address,
    validate_adult_age,
    validate_password_length,
)


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['full_name', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_full_name(self):
        return normalize_full_name(self.cleaned_data['full_name'])

    def clean_email(self):
        return normalize_gmail_address(self.cleaned_data['email'])

    def clean_age(self):
        return validate_adult_age(self.cleaned_data['age'])

    def clean_password(self):
        return validate_password_length(self.cleaned_data['password'])

    def save(self, commit=True):
        registration = super().save(commit=False)
        registration.password = make_password(self.cleaned_data['password'])
        if commit:
            registration.save()
        return registration
