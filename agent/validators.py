from django.core.exceptions import ValidationError

def validate_file_size(value):
    """
    Validate that uploaded file size is not greater than 5MB
    """
    filesize = value.size
    max_size_mb = 5
    max_size_bytes = max_size_mb * 1024 * 1024  # 5MB in bytes
    
    if filesize > max_size_bytes:
        raise ValidationError(f"Maximum file size is {max_size_mb}MB. Your file is {filesize / (1024 * 1024):.2f}MB.")
    return value
