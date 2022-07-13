from rest_framework.routers import DefaultRouter
from ROLESORG.views import *

router = DefaultRouter()

router.register('RolesOrg', RolesOrg, basename = 'RolesOrg')
router.register('ListarRolesXOMC23N2', ListarRolesXOMC23N2, basename = 'ListarRolesXOMC23N2')
router.register('ListarRolesXOMC23N3', ListarRolesXOMC23N3, basename = 'ListarRolesXOMC23N3')
router.register('ListarRolesXOMC23N4', ListarRolesXOMC23N4, basename = 'ListarRolesXOMC23N4')

urlpatterns = router.urls