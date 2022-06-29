from rest_framework import serializers
from usuarios.models import *

#SERIALIZERS PARA EL MANEJO DE LOS USUARIOS
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','Correo','Nombre','Apellidos', 'Rol')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
        usuario = User(**validated_data)
        usuario.set_password(validated_data['password']) #this encrypts the password 
        usuario.save()
        return usuario

    def update(self,instance,validated_data):
        usuario_actualizado = super().update(instance,validated_data) #this encrypts the password 
        usuario_actualizado.set_password(validated_data['password'])
        usuario_actualizado.save()
        return usuario_actualizado

class ListarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'Correo': instance['Correo'],
            'password': instance['password'],
            'Nombre': instance['Nombre'],
            'Apellidos': instance['Apellidos'],
            'Genero': instance['Genero'],
            'Rol': instance['Rol'],
            'fechaCreacion': instance['fechaCreacion'],
            'last_login': instance['last_login']
        }

# SERIALIZERS PARA MANEJAR TABLAS SECUNDARIOAS DE USUARIOS
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class DatosLaboralesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosLaborales
        fields = '__all__'

# SERIALIZERS PARA MANEJAR TABLAS EXTRAS DE USUARIOS
class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mundeleg
        fields = '__all__'

class CPSerializer(serializers.ModelSerializer):
    class Meta:
        model = CP
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

