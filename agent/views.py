from django.shortcuts import render
from rest_framework import generics
from .serializers import AgentProfileSerializer
from .models import AgentProfile
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class AgentProfileCreateView(generics.CreateAPIView):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if hasattr(request.user, 'agent_profile'):
            return Response({"detail": "Agent profile already exists."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)