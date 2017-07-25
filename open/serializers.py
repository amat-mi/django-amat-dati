# coding: utf-8
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from pinf.models import PinfTopoViario, PinfControlloPilomat, PinfControlloVarchi, PinfTopoCiviciaree, \
  PinfDisciplinaAree
from pinf.serializers import PinfTopoViarioSerializer, \
  PinfSostaGiallobluSerializer, PinfSostaInvalidiSerializer, \
  PinfSostaMerciSerializer, PinfSostaTuristiciSerializer, \
  PinfControlloPilomatSerializer, PinfControlloVarchiSerializer, PinfTopoCiviciareeSerializer


#################################################
class GeoJSONOpenDisciplinaAreeSerializer(GeoFeatureModelSerializer):
  pass

  class Meta:
    model = PinfDisciplinaAree
    geo_field = 'geom'

#################################################
class OpenTopoViarioSostaSerializer(PinfTopoViarioSerializer):
  sosta_gialloblu = PinfSostaGiallobluSerializer(many=True)
  sosta_invalidi = PinfSostaInvalidiSerializer(many=True)
  sosta_merci = PinfSostaMerciSerializer(many=True)
  sosta_turistici = PinfSostaTuristiciSerializer(many=True)

  class Meta:
    model = PinfTopoViario
    fields = PinfTopoViarioSerializer.Meta.fields + ['sosta_gialloblu','sosta_invalidi','sosta_merci','sosta_turistici']

#################################################
class OpenTopoViarioControlloSerializer(PinfTopoViarioSerializer):
  controllo_pilomat = PinfControlloPilomatSerializer(many=True)
  controllo_varchi = PinfControlloVarchiSerializer(many=True)

  class Meta:
    model = PinfTopoViario
    fields = PinfTopoViarioSerializer.Meta.fields + ['controllo_pilomat','controllo_varchi']

#################################################
class OpenTopoCiviciareeSerializer(PinfTopoCiviciareeSerializer):
  pass

  class Meta:
    model = PinfTopoCiviciaree
    exclude = ['geom']        #NEVER SEND GEOMETRIES OF CIVICI (even if projected)!!!

