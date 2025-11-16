from .views import AgentProfileCreateView
from django.urls import path


urlpatterns = [
    path('agent-verification', AgentProfileCreateView.as_view(), name='agent_verification'),
]