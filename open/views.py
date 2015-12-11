# coding: utf-8

from oauth2_provider.ext.rest_framework.authentication import OAuth2Authentication
from oauth2_provider.ext.rest_framework.permissions import TokenHasScope
from rest_framework import filters
from rest_framework.decorators import detail_route
from rest_framework.throttling import UserRateThrottle

from open.serializers import OpenTopoViarioSostaSerializer, OpenTopoViarioControlloSerializer
from pinf.views import PinfDisciplinaAreeViewSet, \
  PinfTopoViarioViewSet, PinfSostaMerciViewSet, PinfSostaGiallobluViewSet, \
  PinfSostaInvalidiViewSet, PinfSostaTuristiciViewSet, \
  PinfControlloPilomatViewSet, PinfControlloVarchiViewSet


#################################################
class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'

class SustainedRateThrottle(UserRateThrottle):
    scope = 'sustained'

class ThrottledMixin(object):
    u"""
    Add this mixin to a DRF View or ViewSet to apply throttling only to list action.
    Must be specified before the View or ViewSet parent class.
    """
    def get_throttles(self):
#         throttle_classes = (BurstRateThrottle,SustainedRateThrottle,) if self.action in ['list'] else () 
#         return [throttle() for throttle in throttle_classes]
        return []

#################################################
class TopoMasterFilterMixin(object):
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_fields = ('id',)
    search_fields = ('nome',)
    ordering_fields = ('id', 'nome')  

#################################################
class TopoSlaveFilterMixin(object):
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_fields = ('id_via',)
    search_fields = ('dove',)
    ordering_fields = ('id_via', 'dove')  

#################################################
class OpenPermissionMixin(object):
    authentication_classes = [OAuth2Authentication]
#     permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    permission_classes = [TokenHasScope]
    required_scopes = ['open']

#################################################
class OpenDisciplinaAreeViewSet(ThrottledMixin,
                                OpenPermissionMixin,
                                PinfDisciplinaAreeViewSet):
  pass

#################################################
class OpenTopoViarioViewSet(ThrottledMixin,TopoMasterFilterMixin,
                            OpenPermissionMixin,
                            PinfTopoViarioViewSet):
    @detail_route(serializer_class=OpenTopoViarioSostaSerializer)
    def sosta(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @detail_route(serializer_class=OpenTopoViarioControlloSerializer)
    def controllo(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

#################################################
class OpenSostaGiallobluViewSet(ThrottledMixin,TopoSlaveFilterMixin,
                                OpenPermissionMixin,
                                PinfSostaGiallobluViewSet):
  pass

#################################################
class OpenSostaInvalidiViewSet(ThrottledMixin,TopoSlaveFilterMixin,
                               OpenPermissionMixin,
                               PinfSostaInvalidiViewSet):
  pass

#################################################
class OpenSostaMerciViewSet(ThrottledMixin,TopoSlaveFilterMixin,
                            OpenPermissionMixin,
                            PinfSostaMerciViewSet):
  pass

#################################################
class OpenSostaTuristiciViewSet(ThrottledMixin,TopoSlaveFilterMixin,
                                OpenPermissionMixin,
                                PinfSostaTuristiciViewSet):
  pass

#################################################
class OpenControlloPilomatViewSet(ThrottledMixin,TopoSlaveFilterMixin,
                                 OpenPermissionMixin,
                                 PinfControlloPilomatViewSet):
  pass

#################################################
class OpenControlloVarchiViewSet(ThrottledMixin,TopoSlaveFilterMixin,
                                 OpenPermissionMixin,
                                 PinfControlloVarchiViewSet):
  pass
