# coding: utf-8
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.throttling import UserRateThrottle

from pinf.models import PinfSostaMerci
from pinf.serializers import PinfSostaMerciSerializer

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
    
    def list(self, request):
        u"""
        Returns all instances with Pagination but no Throttling.
        """
        return super(OpenSostaMerciViewSet, self).list(request)
      
    @list_route(
                paginate_by = None,
                throttle_classes = (BurstRateThrottle,SustainedRateThrottle,)
                )
    def all(self, request):
        u"""
        Returns all instances with Throttling but no Pagination.
        """
        return super(OpenSostaMerciViewSet, self).list(request)
