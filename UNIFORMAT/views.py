from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

# Create your views here.

#CRUD DEL NIVEL 1 DE UNIFORMAT
class ListarUFTCategorias(ListAPIView):
    serializer_class = UFTCategoriaSerializer
    queryset = UFTCategorias.objects.all()

class CrearCategoria(CreateAPIView):
    serializer_class = UFTCategoriaSerializer
    queryset = UFTCategorias.objects.all()

class EditarCategoria(RetrieveUpdateAPIView):
    serializer_class = UFTCategoriaSerializer
    queryset = UFTCategorias.objects.all()

class EliminarCatgoria(DestroyAPIView): #para eliminar no es requerido enviar todo el json, sino con el puro id (llave primaria)
    serializer_class = UFTCategoriaSerializer
    queryset = UFTCategorias.objects.all()

#CRUD DEL NIVEL 2 DE UNIFORMAT
class ListarUFTNivel2(ListAPIView):
    serializer_class = UFTNivel2Serializer
    queryset = UFTNivel2.objects.all()

class CrearUFTNivel2(CreateAPIView):
    serializer_class = UFTNivel2Serializer
    queryset = UFTNivel2.objects.all()

class EditarUFTNivel2(RetrieveUpdateAPIView):
    serializer_class = UFTNivel2Serializer
    queryset = UFTNivel2.objects.all()

class EliminarUFTNivel2(DestroyAPIView): #para eliminar no es requerido enviar todo el json, sino con el puro id (llave primaria)
    serializer_class = UFTNivel2Serializer
    queryset = UFTNivel2.objects.all()

#CRUD DEL NIVEL 3 DE UNIFORMAT
class ListarUFTNivel3(ListAPIView):
    serializer_class = UFTNivel3Serializer
    queryset = UFTNivel3.objects.all()

class CrearUFTNivel3(CreateAPIView):
    serializer_class = UFTNivel3Serializer
    queryset = UFTNivel3.objects.all()

class EditarUFTNivel3(RetrieveUpdateAPIView):
    serializer_class = UFTNivel3Serializer
    queryset = UFTNivel3.objects.all()

class EliminarUFTNivel3(DestroyAPIView): #para eliminar no es requerido enviar todo el json, sino con el puro id (llave primaria)
    serializer_class = UFTNivel3Serializer
    queryset = UFTNivel3.objects.all()

#CRUD DEL NIVEL 4 DE UNIFORMAT
class ListarUFTNivel4(ListAPIView):
    serializer_class = UFTNivel4Serializer
    queryset = UFTNivel4.objects.all()

class CrearUFTNivel4(CreateAPIView):
    serializer_class = UFTNivel4Serializer
    queryset = UFTNivel4.objects.all()

class EditarUFTNivel4(RetrieveUpdateAPIView):
    serializer_class = UFTNivel4Serializer
    queryset = UFTNivel4.objects.all()

class EliminarUFTNivel4(DestroyAPIView): #para eliminar no es requerido enviar todo el json, sino con el puro id (llave primaria)
    serializer_class = UFTNivel4Serializer
    queryset = UFTNivel4.objects.all()

#CRUD DEL NIVEL 5 DE UNIFORMAT
class ListarUFTNivel5(ListAPIView):
    serializer_class = UFTNivel5Serializer
    queryset = UFTNivel5.objects.all()

class CrearUFTNivel5(CreateAPIView):
    serializer_class = UFTNivel5Serializer
    queryset = UFTNivel5.objects.all()

class EditarUFTNivel5(RetrieveUpdateAPIView):
    serializer_class = UFTNivel5Serializer
    queryset = UFTNivel5.objects.all()

class EliminarUFTNivel5(DestroyAPIView): #para eliminar no es requerido enviar todo el json, sino con el puro id (llave primaria)
    serializer_class = UFTNivel5Serializer
    queryset = UFTNivel5.objects.all()