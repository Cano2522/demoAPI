from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView

)
from OMNICLAS41.models import *
from OMNICLAS41.serializers import *


# Create your views here.

#TABLA OMNICLASS 41

class ListarOmniclass41(ListAPIView):
    queryset = OmniClass41.objects.all()
    serializer_class = OmniClass41Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOmniclass41(CreateAPIView):
    queryset = OmniClass41.objects.all()
    serializer_class = OmniClass41Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOmniclass41(UpdateAPIView):
    queryset = OmniClass41.objects.all()
    serializer_class = OmniClass41Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOmniclass41(DestroyAPIView):
    queryset = OmniClass41.objects.all()
    serializer_class = OmniClass41Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#TABLA OMNICLASS 41 NIVEL 1

class ListarOMC41Nivel1(ListAPIView):
    queryset = OMC41Nivel1.objects.all()
    serializer_class = OMC41Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel1(CreateAPIView):
    queryset = OMC41Nivel1.objects.all()
    serializer_class = OMC41Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel1(UpdateAPIView):
    queryset = OMC41Nivel1.objects.all()
    serializer_class = OMC41Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel1(DestroyAPIView):
    queryset = OMC41Nivel1.objects.all()
    serializer_class = OMC41Nivel1Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#TABLA OMNICLASS 41 NIVEL 2

class ListarOMC41Nivel2(ListAPIView):
    queryset = OMC41Nivel2.objects.all()
    serializer_class = OMC41Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel2(CreateAPIView):
    queryset = OMC41Nivel2.objects.all()
    serializer_class = OMC41Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel2(UpdateAPIView):
    queryset = OMC41Nivel2.objects.all()
    serializer_class = OMC41Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel2(DestroyAPIView):
    queryset = OMC41Nivel2.objects.all()
    serializer_class = OMC41Nivel2Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#TABLA OMNICLASS 41 NIVEL 3

class ListarOMC41Nivel3(ListAPIView):
    queryset = OMC41Nivel3.objects.all()
    serializer_class = OMC41Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel3(CreateAPIView):
    queryset = OMC41Nivel3.objects.all()
    serializer_class = OMC41Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel3(UpdateAPIView):
    queryset = OMC41Nivel3.objects.all()
    serializer_class = OMC41Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel3(DestroyAPIView):
    queryset = OMC41Nivel3.objects.all()
    serializer_class = OMC41Nivel3Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#TABLA OMNICLASS 41 NIVEL 4

class ListarOMC41Nivel4(ListAPIView):
    queryset = OMC41Nivel4.objects.all()
    serializer_class = OMC41Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel4(CreateAPIView):
    queryset = OMC41Nivel4.objects.all()
    serializer_class = OMC41Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel4(UpdateAPIView):
    queryset = OMC41Nivel4.objects.all()
    serializer_class = OMC41Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel4(DestroyAPIView):
    queryset = OMC41Nivel4.objects.all()
    serializer_class = OMC41Nivel4Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#TABLA OMNICLASS 41 NIVEL 5

class ListarOMC41Nivel5(ListAPIView):
    queryset = OMC41Nivel5.objects.all()
    serializer_class = OMC41Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel5(CreateAPIView):
    queryset = OMC41Nivel5.objects.all()
    serializer_class = OMC41Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel5(UpdateAPIView):
    queryset = OMC41Nivel5.objects.all()
    serializer_class = OMC41Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel5(DestroyAPIView):
    queryset = OMC41Nivel5.objects.all()
    serializer_class = OMC41Nivel5Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#TABLA OMNICLASS 41 NIVEL 6

class ListarOMC41Nivel6(ListAPIView):
    queryset = OMC41Nivel6.objects.all()
    serializer_class = OMC41Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearOMC41Nivel6(CreateAPIView):
    queryset = OMC41Nivel6.objects.all()
    serializer_class = OMC41Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditarOMC41Nivel6(UpdateAPIView):
    queryset = OMC41Nivel6.objects.all()
    serializer_class = OMC41Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EliminarOMC41Nivel6(DestroyAPIView):
    queryset = OMC41Nivel6.objects.all()
    serializer_class = OMC41Nivel6Serializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
