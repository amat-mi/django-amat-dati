# coding: utf-8
from pinf.models import PinfTopoViario
from pinf.serializers import PinfTopoViarioSerializer, \
  PinfSostaGiallobluSerializer, PinfSostaInvalidiSerializer, \
  PinfSostaMerciSerializer, PinfSostaTuristiciSerializer


#################################################
class OpenTopoViarioSostaSerializer(PinfTopoViarioSerializer):
  sosta_gialloblu = PinfSostaGiallobluSerializer()
  sosta_invalidi = PinfSostaInvalidiSerializer()
  sosta_merci = PinfSostaMerciSerializer()
  sosta_turistici = PinfSostaTuristiciSerializer()

  class Meta:
    model = PinfTopoViario
    fields = PinfTopoViarioSerializer.Meta.fields + ['sosta_gialloblu','sosta_invalidi','sosta_merci','sosta_turistici']
