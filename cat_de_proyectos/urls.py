

from django.urls import path,include
from proyectosapp import views
from django.urls import include, path
from rest_framework import routers
from users import views1


router = routers.DefaultRouter()
router.register(r'registro',views1.GuardarUserSerializer)
router.register(r'proyectosapp', views.ProViewSet)
router.register(r'incidencias', views.InsiViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]

