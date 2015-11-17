# coding: utf-8

from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from pinf.views import PinfSostaGiallobluViewSet, PinfSostaInvalidiViewSet, \
  PinfSostaMerciViewSet, PinfSostaTuristiciViewSet


router = SimpleRouter()

##### Elenco endpoints ################################
router.register(r'sosta/gialloblu', PinfSostaGiallobluViewSet)
router.register(r'sosta/invalidi', PinfSostaInvalidiViewSet)
router.register(r'sosta/merci', PinfSostaMerciViewSet)
router.register(r'sosta/turistici', PinfSostaTuristiciViewSet)


##### Aggiunta degli url ####################################
urlpatterns =  patterns('',
    url(r'^', include(router.urls)),    
)
