# coding: utf-8
from rest_framework import viewsets
from rest_framework.decorators import list_route, throttle_classes
from rest_framework.throttling import UserRateThrottle

from pinf.models import PinfSostaMerci
from pinf.serializers import PinfSostaMerciSerializer
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
        """
        return super(OpenSostaMerciViewSet, self).list(request)
