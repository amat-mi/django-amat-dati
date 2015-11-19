# coding: utf-8

from django.http.response import HttpResponse, HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.response import Response

from pinf.models import PinfTopoViario, PinfTopoCiviciaree, \
  PinfSostaGialloblu, PinfSostaInvalidi, PinfSostaMerci, \
  PinfSostaTuristici, PinfControlloVarchi
from pinf.serializers import PinfTopoViarioSerializer, PinfTopoCiviciareeSerializer, \
  PinfSostaGiallobluSerializer, \
  PinfSostaInvalidiSerializer, PinfSostaMerciSerializer, \
  PinfSostaTuristiciSerializer, PinfControlloVarchiSerializer


#################################################
def build_message_response(message,status=HttpResponse.status_code):
  return Response({'message': message},status=status)

#################################################
class RESPERR(object):
  GENERIC_ERROR = 'GENERIC_ERROR'

def build_error_response(error,status=HttpResponseBadRequest.status_code,message=None):
  return Response({'error': error, 'message': message},status=status)

#################################################
def build_exception_response(error=RESPERR.GENERIC_ERROR,status=HttpResponseBadRequest.status_code):
    import traceback
    return build_error_response(error,status,message=traceback.format_exc())

#################################################
class PinfTopoViarioViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfTopoViarioSerializer
    queryset = PinfTopoViario.objects.all()
    paginate_by = None

#################################################
class PinfTopoCiviciareeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfTopoCiviciareeSerializer
    queryset = PinfTopoCiviciaree.objects.all()
    paginate_by = None

#################################################
class PinfSostaGiallobluViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfSostaGiallobluSerializer
    queryset = PinfSostaGialloblu.objects.all()
    paginate_by = None

#################################################
class PinfSostaInvalidiViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfSostaInvalidiSerializer
    queryset = PinfSostaInvalidi.objects.all()
    paginate_by = None

#################################################
class PinfSostaMerciViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfSostaMerciSerializer
    queryset = PinfSostaMerci.objects.all()
    paginate_by = None

#################################################
class PinfSostaTuristiciViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfSostaTuristiciSerializer
    queryset = PinfSostaTuristici.objects.all()
    paginate_by = None

#################################################
class PinfControlloVarchiViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfControlloVarchiSerializer
    queryset = PinfControlloVarchi.objects.all()
    paginate_by = None
