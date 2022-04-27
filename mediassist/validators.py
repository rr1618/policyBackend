from django.core.exceptions import ValidationError


def validate_premium(value):
    if value > 1000000:
        raise ValidationError('Premium should be less than 1 million')