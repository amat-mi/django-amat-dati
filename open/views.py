# coding: utf-8

from rest_framework import filters
from rest_framework.decorators import detail_route
from rest_framework.throttling import UserRateThrottle

from open.serializers import OpenTopoViarioSostaSerializer, OpenTopoViarioControlloSerializer
from pinf.views import PinfTopoViarioViewSet, PinfSostaMerciViewSet, PinfSostaGiallobluViewSet, \
  PinfSostaInvalidiViewSet, PinfSostaTuristiciViewSet, PinfControlloVarchiViewSet


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
class OpenTopoViarioViewSet(ThrottledMixin,TopoMasterFilterMixin,PinfTopoViarioViewSet):
    @detail_route(serializer_class=OpenTopoViarioSostaSerializer)
    def sosta(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @detail_route(serializer_class=OpenTopoViarioControlloSerializer)
    def controllo(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

#################################################
class OpenSostaGiallobluViewSet(ThrottledMixin,TopoSlaveFilterMixin,PinfSostaGiallobluViewSet):
  pass

#################################################
class OpenSostaInvalidiViewSet(ThrottledMixin,TopoSlaveFilterMixin,PinfSostaInvalidiViewSet):
  pass

#################################################
class OpenSostaMerciViewSet(ThrottledMixin,TopoSlaveFilterMixin,PinfSostaMerciViewSet):
  pass

#################################################
class OpenSostaTuristiciViewSet(ThrottledMixin,TopoSlaveFilterMixin,PinfSostaTuristiciViewSet):
  pass

#################################################
class OpenControlloVarchiViewSet(ThrottledMixin,TopoSlaveFilterMixin,PinfControlloVarchiViewSet):
  pass

# #################################################
# class OpenSostaViewSet(viewsets.GenericViewSet):
#     serializer_class = PinfSostaGiallobluSerializer
# #     queryset = PinfSostaMerci.objects.all()
#     paginate_by = 10
#     filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
#     filter_fields = ('tipo',)
#     search_fields = ('dove', '=id_via',)
# 
#     def _list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
# 
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
# 
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
# 
#     def _retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
# 
#     @list_route(
#         serializer_class = PinfSostaGiallobluSerializer,
#         queryset = PinfSostaGialloblu.objects.all(),
#         throttle_classes = (BurstRateThrottle,SustainedRateThrottle,)
#                 )
#     def gialloblu(self, request, *args, **kwargs):
#         return self._list(request, *args, **kwargs)
#       
#     @list_route(
#         serializer_class = PinfSostaInvalidiSerializer,
#         queryset = PinfSostaInvalidi.objects.all(),
#         throttle_classes = (BurstRateThrottle,SustainedRateThrottle,)
#                 )
#     def invalidi(self, request, *args, **kwargs):
#         return self._list(request, *args, **kwargs)
#       
#     @list_route(
#         serializer_class = PinfSostaMerciSerializer,
#         queryset = PinfSostaMerci.objects.all(),
#         throttle_classes = (BurstRateThrottle,SustainedRateThrottle,)
#                 )
#     def merci(self, request, *args, **kwargs):
#         return self._list(request, *args, **kwargs)
# 
#     @detail_route(
#         serializer_class = PinfSostaMerciSerializer,
#         queryset = PinfSostaMerci.objects.all(),
#         paginate_by = None,
#         throttle_classes = ()
#                 )
#     def merci_single(self, request, *args, **kwargs):
#         return self._retrieve(request, *args, **kwargs)
# 
#     @list_route(
#         serializer_class = PinfSostaTuristiciSerializer,
#         queryset = PinfSostaTuristici.objects.all(),
#         paginate_by = None,
#         throttle_classes = (),
#                 )
#     def turistici(self, request, *args, **kwargs):
#         return self._list(request, *args, **kwargs)
