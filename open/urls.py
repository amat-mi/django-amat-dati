# coding: utf-8

from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from open.views import OpenDisciplinaAreeViewSet, \
  OpenTopoViarioViewSet, OpenSostaGiallobluViewSet, OpenSostaInvalidiViewSet, \
  OpenSostaMerciViewSet, OpenSostaTuristiciViewSet, \
  OpenControlloPilomatViewSet, OpenControlloVarchiViewSet


router = SimpleRouter()

##### Elenco endpoints ################################
router.register(r'disciplina_aree', OpenDisciplinaAreeViewSet)

router.register(r'topo_viario', OpenTopoViarioViewSet)

router.register(r'sosta_gialloblu', OpenSostaGiallobluViewSet)
router.register(r'sosta_invalidi', OpenSostaInvalidiViewSet)
router.register(r'sosta_merci', OpenSostaMerciViewSet)
router.register(r'sosta_turistici', OpenSostaTuristiciViewSet)

router.register(r'controllo_pilomat', OpenControlloPilomatViewSet)
router.register(r'controllo_varchi', OpenControlloVarchiViewSet)

##### Aggiunta degli url ####################################
urlpatterns =  patterns('',
    url(r'^', include(router.urls)),    
)
