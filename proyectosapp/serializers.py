from rest_framework import serializers
from proyectosapp.models import Proyectos,Insidencias


class ProySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = ['id', 'titulo', 'fecha_de_entrega', 'language', 'style']


class InsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insidencias
        fields = ['id','fe_creacion','nombre','direccion',
    'telefono','id_proyecto','style']

