from proyectosapp.models import Proyectos,Insidencias
from proyectosapp.serializers import ProySerializer,InsiSerializer

from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics

"""declaracion de la clase viewset que se utiliza para los metodos post delete get put"""
class ProViewSet(viewsets.ModelViewSet):

    queryset = Proyectos.objects.all()
    serializer_class = ProySerializer

    permission_classes = [permissions.IsAuthenticated]

class InsiViewSet(viewsets.ModelViewSet):
    
    queryset = Insidencias.objects.all()
    serializer_class = InsiSerializer
    permission_classes = [permissions.IsAuthenticated]