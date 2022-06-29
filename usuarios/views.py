from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from usuarios.models import User
from usuarios.serializers import *

#VISTAS PARA EL CONTROL DE LA TABLA "User" que es la principal para el logeo y manejo de tokens
# Create your views here.
@api_view(['GET','POST'])
def VistaUsuario(request):
    if request.method == 'GET':
        usuarios = User.objects.all().values('id','username','Correo','password','Nombre','Apellidos','Genero','Rol','fechaCreacion','last_login')
        usuarios_serializer = ListarUsuarioSerializer(usuarios,many = True)
        
        return Response(usuarios_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        usuario_serializer = UsuarioSerializer(data = request.data)

        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response({'mensaje':'Usuario creado correctamente!'}, status = status.HTTP_201_CREATED)
        
        return Response(usuario_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def VistaUsuarioDetalle(request,pk=None):
    usuario = User.objects.filter(id=pk).first()

    if usuario:

        if request.method == 'GET':
            usuario_serializer = UsuarioSerializer(usuario)
            return Response(usuario_serializer.data, status = status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            usuario_serializer = UsuarioSerializer(instance = usuario, data = request.data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response(usuario_serializer.data, status = status.HTTP_200_OK)
            return Response(usuario_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            usuario.delete()
            return Response({'mensaje':'Usuario eliminado correctamente!'}, status = status.HTTP_200_OK)

    return Response({'mensaje':'No se a encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

#VISTAS PARA EL CONTROL DE LAS TABLAS SECUNDARIAS DE USUARIOS

class VistaEmpleado(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idEmpleado = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idEmpleado=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

class VistaDatosLaborales(viewsets.ModelViewSet):
    serializer_class = DatosLaboralesSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idDatosLab = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idDatosLab=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#VISTAS PARA EL CONTROL DE LAS TABLAS EXTRAS DE USUARIOS

class VistaCP(viewsets.ModelViewSet):
    serializer_class = CPSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(cp = pk).first()

class VistaCargo(viewsets.ModelViewSet):
    serializer_class = CargoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idCargo = pk).first()

class VistaDepartamento(viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idDepto = pk).first()

class VistaContrato(viewsets.ModelViewSet):
    serializer_class = ContratoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idContrato = pk).first()

