# coding: utf-8

from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from open.views import OpenTopoViarioViewSet, OpenSostaGiallobluViewSet, OpenSostaInvalidiViewSet, \
  OpenSostaMerciViewSet, OpenSostaTuristiciViewSet, OpenControlloVarchiViewSet


router = SimpleRouter()

##### Elenco endpoints ################################
router.register(r'topo_viario', OpenTopoViarioViewSet)

router.register(r'sosta_gialloblu', OpenSostaGiallobluViewSet)
router.register(r'sosta_invalidi', OpenSostaInvalidiViewSet)
router.register(r'sosta_merci', OpenSostaMerciViewSet)
router.register(r'sosta_turistici', OpenSostaTuristiciViewSet)

router.register(r'controllo_varchi', OpenControlloVarchiViewSet)

##### Aggiunta degli url ####################################
urlpatterns =  patterns('',
    url(r'^', include(router.urls)),    
)
