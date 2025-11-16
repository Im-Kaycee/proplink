from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import AgentProfile
from django.core.exceptions import ValidationError as DjangoValidationError

class AgentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ['NIN', 'selfie_with_id', 'guarantor_name', 'guarantor_contact',
                  'guarantor_address', 'relation_to_guarantor', 'guarantor_passport_photo',
                  'agency_name', 'is_verified']

    def validate_NIN(self, value):
        if AgentProfile.objects.filter(NIN=value).exists():
            raise serializers.ValidationError("An agent with this NIN already exists.")
        return value
    def validate_selfie_with_id(self, value):
        if value.size > 5 * 1024 * 1024:  # 5MB
            raise serializers.ValidationError("File size cannot exceed 5MB.")
        return value
    
    def validate_guarantor_passport_photo(self, value):
        if value.size > 5 * 1024 * 1024:  # 5MB
            raise serializers.ValidationError("File size cannot exceed 5MB.")
        return value