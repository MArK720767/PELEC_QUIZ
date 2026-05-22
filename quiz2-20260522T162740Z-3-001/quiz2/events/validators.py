from django.core.exceptions import ValidationError


def normalize_full_name(value):
    full_name = value.strip()
    if len(full_name) < 5:
        raise ValidationError('Full name must be at least 5 characters.')
    return full_name


def normalize_gmail_address(value):
    email = value.strip().lower()
    if not email.endswith('@gmail.com'):
        raise ValidationError('Email must end with @gmail.com.')
    return email


def validate_adult_age(value):
    if value < 18:
        raise ValidationError('Age must be 18 and above.')
    return value


def validate_password_length(value):
    if len(value) < 8:
        raise ValidationError('Password must be at least 8 characters.')
    return value
