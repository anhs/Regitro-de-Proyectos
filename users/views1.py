from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from users.serializers import GuardarUserSerializer
from rest_framework import generics


class GuardarUserSerializer(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = GuardarUserSerializer
    #permission_classes = [permissions.IsAuthenticated]

