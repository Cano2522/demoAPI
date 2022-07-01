from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import *

router = DefaultRouter()
router.register('Empleados', VistaEmpleado, basename = 'VistaEmpleado')
router.register('DatosLaborales', VistaDatosLaborales, basename = 'VistaDatosLaborales')
router.register('CodigoPostal', VistaCP, basename = 'VistaCP')
router.register('Municipio', VistaMunDeleg, basename = 'VistaMunDeleg')
router.register('Estado', VistaEstado, basename = 'VistaEstado')
router.register('Pais', VistaPais, basename = 'VistaPais')
router.register('Departamento', VistaDepartamento, basename = 'VistaDepartamento')
router.register('Cargo', VistaCargo, basename = 'VistaCargo')
router.register('Contrato', VistaContrato, basename = 'VistaContrato')


urlpatterns = [
    # path('usuario/',UserAPIView.as_view(), name = 'usuario_api')
    path('',include(router.urls)),
    path('Listar/',VistaUsuario, name = 'ListarUsuario'),
    path('Crear/',VistaUsuario, name = 'CrearUsuario'),
    path('Editar/<int:pk>/',VistaUsuarioDetalle, name = 'EditarUsuario'),
    path('Eliminar/<int:pk>/',VistaUsuarioDetalle, name = 'EliminarUsuario')
]