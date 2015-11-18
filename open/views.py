# coding: utf-8
from rest_framework import viewsets, filters
from rest_framework.decorators import list_route, throttle_classes, detail_route
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from pinf.models import PinfSostaMerci, PinfSostaTuristici, PinfSostaGialloblu, \
  PinfSostaInvalidi
from pinf.serializers import PinfSostaMerciSerializer, \
  PinfSostaGiallobluSerializer, PinfSostaTuristiciSerializer, \
  PinfSostaInvalidiSerializer
from pinf.views import PinfSostaMerciViewSet


#################################################
class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'

class SustainedRateThrottle(UserRateThrottle):
    scope = 'sustained'

#################################################
class OpenSostaMerciViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfSostaMerciSerializer
    queryset = PinfSostaMerci.objects.all()
    paginate_by = 10
#     throttle_classes = (BurstRateThrottle,SustainedRateThrottle,)
    
    def get_throttles(self):
        """
        Instantiates and returns the list of throttles that this view uses based upon which action was called.
        """
        throttle_classes = (BurstRateThrottle,SustainedRateThrottle,) if self.action in ['list'] else () 
        return [throttle() for throttle in throttle_classes]
    
# #     @throttle_classes((BurstRateThrottle,SustainedRateThrottle,))    
#     def list(self, request, *args, **kwargs):
#         u"""
#         Returns all instances with Pagination but no Throttling.
#         """
#         return super(OpenSostaMerciViewSet, self).list(request, *args, **kwargs)
#     list.throttle_classes = (BurstRateThrottle,SustainedRateThrottle,)
      
#     @list_route(
#                 paginate_by = None,
#                 throttle_classes = (BurstRateThrottle,SustainedRateThrottle,)
#                 )
#     @list_route(
#                 throttle_classes = ()
#                 )
    @list_route()
    def all(self, request):
        u"""
        Returns all instances with Throttling but no Pagination.
        ---
          # YAML (must be separated by `---`)
      
#           serializer: .serializers.FooSerializer
          omit_serializer: true
          
          type:
            name:
              required: true
              type: string
            url:
              required: false
              type: url                  
        """
        return super(OpenSostaMerciViewSet, self).list(request)

#################################################
class OpenSostaViewSet(viewsets.GenericViewSet):
    serializer_class = PinfSostaGiallobluSerializer
#     queryset = PinfSostaMerci.objects.all()
    paginate_by = 10
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('tipo',)
    search_fields = ('dove', '=id_via',)

    def _list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def _retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @list_route(
        serializer_class = PinfSostaGiallobluSerializer,
        queryset = PinfSostaGialloblu.objects.all(),
        throttle_classes = (BurstRateThrottle,SustainedRateThrottle,)
                )
    def gialloblu(self, request, *args, **kwargs):
        return self._list(request, *args, **kwargs)
      
    @list_route(
        serializer_class = PinfSostaInvalidiSerializer,
        queryset = PinfSostaInvalidi.objects.all(),
        throttle_classes = (BurstRateThrottle,SustainedRateThrottle,)
                )
    def invalidi(self, request, *args, **kwargs):
        return self._list(request, *args, **kwargs)
      
    @list_route(
        serializer_class = PinfSostaMerciSerializer,
        queryset = PinfSostaMerci.objects.all(),
        throttle_classes = (BurstRateThrottle,SustainedRateThrottle,)
                )
    def merci(self, request, *args, **kwargs):
        return self._list(request, *args, **kwargs)

    @detail_route(
        serializer_class = PinfSostaMerciSerializer,
        queryset = PinfSostaMerci.objects.all(),
        paginate_by = None,
        throttle_classes = ()
                )
    def merci_single(self, request, *args, **kwargs):
        return self._retrieve(request, *args, **kwargs)

    @list_route(
        serializer_class = PinfSostaTuristiciSerializer,
        queryset = PinfSostaTuristici.objects.all(),
        paginate_by = None,
        throttle_classes = (),
                )
    def turistici(self, request, *args, **kwargs):
        return self._list(request, *args, **kwargs)
