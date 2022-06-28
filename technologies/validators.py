import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    print(value, "value")
    ext = os.path.splitext(value.name)[1]  # [0] returns path and filename
    valid_extensions = ['.svg', '.png', '.jpg', '.webl'] # populate with the allowed extensions
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')