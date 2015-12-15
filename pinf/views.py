# coding: utf-8

from django.http.response import HttpResponse, HttpResponseBadRequest
from oauth2_provider.ext.rest_framework.authentication import OAuth2Authentication
from oauth2_provider.ext.rest_framework.permissions import TokenHasScope
from rest_framework import viewsets, permissions
from rest_framework.decorators import authentication_classes, list_route
from rest_framework.response import Response

from pinf.massive import build_excel_response
from pinf.models import PinfDisciplinaAree, PinfTopoViario, PinfTopoCiviciaree, \
  PinfSostaGialloblu, PinfSostaInvalidi, PinfSostaMerci, \
  PinfSostaTuristici, PinfControlloPilomat, PinfControlloVarchi
from pinf.serializers import PinfDisciplinaAreeSerializer, \
  PinfTopoViarioSerializer, PinfTopoCiviciareeSerializer, \
  PinfSostaGiallobluSerializer, \
  PinfSostaInvalidiSerializer, PinfSostaMerciSerializer, \
  PinfSostaTuristiciSerializer, \
  PinfControlloPilomatSerializer, PinfControlloVarchiSerializer
from pinf.utils import build_exception_response


#################################################
class PinfPermissionMixin(object):
    authentication_classes = [OAuth2Authentication]
#     permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    permission_classes = [TokenHasScope]
    required_scopes = ['pinf']

#################################################
class PinfDisciplinaAreeViewSet(PinfPermissionMixin,viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfDisciplinaAreeSerializer
    queryset = PinfDisciplinaAree.objects.all()
    paginate_by = None

#################################################
class PinfTopoViarioViewSet(PinfPermissionMixin,viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfTopoViarioSerializer
    queryset = PinfTopoViario.objects.all()
    paginate_by = None

#################################################
class PinfTopoCiviciareeViewSet(PinfPermissionMixin,viewsets.ReadOnlyModelViewSet):
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
class PinfControlloPilomatViewSet(PinfPermissionMixin,viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfControlloPilomatSerializer
    queryset = PinfControlloPilomat.objects.all()
    paginate_by = None

    @list_route(methods=['GET'])
    def download(self, request):
        try:
            serializer = self.get_serializer_class()(self.get_queryset(), many=True)
            return build_excel_response(serializer.child.fields.keys(),serializer.data,'controllo_pilomat')
        except Exception, exc:
            return build_exception_response()

#################################################
class PinfControlloVarchiViewSet(PinfPermissionMixin,viewsets.ReadOnlyModelViewSet):
    serializer_class = PinfControlloVarchiSerializer
    queryset = PinfControlloVarchi.objects.all()
    paginate_by = None
