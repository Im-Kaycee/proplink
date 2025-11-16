from django.db import models
from .validators import validate_file_size
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile')
    NIN = models.CharField(max_length=20, unique=True)
    selfie_with_id = models.ImageField(upload_to='agent_selfies/', validators=[validate_file_size], help_text="Maximum file size is 5MB")
    guarantor_name = models.CharField(max_length=255)
    guarantor_contact = models.CharField(max_length=20)
    guarantor_address = models.CharField(max_length=255)
    relation_to_guarantor = models.CharField(max_length=100)
    guarantor_passport_photo = models.ImageField(upload_to='guarantor_photos/',
        validators=[validate_file_size],
        help_text="Maximum file size: 5MB")
    agency_name = models.CharField(max_length=255, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.agency_name or 'No Agency'}"

    
