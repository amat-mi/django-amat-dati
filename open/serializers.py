# coding: utf-8
from pinf.models import PinfTopoViario, PinfControlloVarchi
from pinf.serializers import PinfTopoViarioSerializer, \
  PinfSostaGiallobluSerializer, PinfSostaInvalidiSerializer, \
  PinfSostaMerciSerializer, PinfSostaTuristiciSerializer, \
  PinfControlloVarchiSerializer


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
  controllo_varchi = PinfControlloVarchiSerializer(many=True)

  class Meta:
    model = PinfTopoViario
    fields = PinfTopoViarioSerializer.Meta.fields + ['controllo_varchi']
