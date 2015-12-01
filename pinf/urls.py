# coding: utf-8

from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from pinf.views import PinfDisciplinaAreeViewSet, \
  PinfTopoViarioViewSet, PinfSostaGiallobluViewSet, PinfSostaInvalidiViewSet, \
  PinfSostaMerciViewSet, PinfSostaTuristiciViewSet, PinfControlloVarchiViewSet, \
  PinfTopoCiviciareeViewSet


router = SimpleRouter()

##### Elenco endpoints ################################
router.register(r'disciplina_aree', PinfDisciplinaAreeViewSet)

router.register(r'topo_viario', PinfTopoViarioViewSet)
router.register(r'topo_civiciaree', PinfTopoCiviciareeViewSet)

router.register(r'sosta_gialloblu', PinfSostaGiallobluViewSet)
router.register(r'sosta_invalidi', PinfSostaInvalidiViewSet)
router.register(r'sosta_merci', PinfSostaMerciViewSet)
router.register(r'sosta_turistici', PinfSostaTuristiciViewSet)

router.register(r'controllo_varchi', PinfControlloVarchiViewSet)

##### Aggiunta degli url ####################################
urlpatterns =  patterns('',
    url(r'^', include(router.urls)),    
)
