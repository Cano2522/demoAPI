from rest_framework.routers import DefaultRouter
from UNIDADESMEDIDA.views import *

router = DefaultRouter()

router.register('TipoUnidadMedida', VistaTipoUniMed, basename = 'VistaTipoUniMed')
router.register('SubtipoUnidadMedida', VistaSubTipUni, basename = 'VistaTipoUniMed')
router.register('UnidadesMedida', VistaUnidadesMedida, basename = 'VistaTipoUniMed')

urlpatterns = router.urls