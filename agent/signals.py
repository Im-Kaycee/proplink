from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AgentProfile

@receiver(post_save, sender=AgentProfile)
def update_user_role_when_agent_verified(sender, instance, created, **kwargs):
    """
    When admin marks an agent as verified, automatically update
    the corresponding user's role to 'agent'.
    """
    if not created:
        if instance.is_verified and instance.user.role != 'agent':
            instance.user.role = 'agent'
            instance.user.save(update_fields=['role'])
        else:
            if not instance.is_verified and instance.user.role == 'agent':
                instance.user.role = 'user'
                instance.user.save(update_fields=['role'])