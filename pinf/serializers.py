# coding: utf-8

from rest_framework import serializers

from pinf.models import PinfDisciplinaAree, PinfTopoViario, PinfTopoCiviciaree, \
  PinfSostaGialloblu, PinfSostaInvalidi, PinfSostaMerci, \
  PinfSostaTuristici, PinfControlloPilomat, PinfControlloVarchi


#################################################
class PinfDisciplinaAreeSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfDisciplinaAree
    fields = '__all__'

#################################################
class PinfTopoViarioSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfTopoViario
    fields = ['id','nome']

#################################################
class PinfTopoCiviciareeSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfTopoCiviciaree
    #NOOO!!! Non escludiamo il campo geometrico, perché tanto è un servizio riservato a pochi!!!
    #ATTENZIONE!!! Per una eventuale pubblicazione come "open" usare OpenTopoCiviciareeSerializer!!!
#     exclude = ['geom']        #NEVER SEND GEOMETRIES OF CIVICI (even if projected)!!!
    fields = '__all__'

#################################################
class PinfSostaGiallobluSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfSostaGialloblu
    fields = '__all__'

#################################################
class PinfSostaInvalidiSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfSostaInvalidi
    fields = '__all__'

#################################################
class PinfSostaMerciSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfSostaMerci
    fields = '__all__'

#################################################
class PinfSostaTuristiciSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfSostaTuristici
    fields = '__all__'

#################################################
class PinfControlloPilomatSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfControlloPilomat
    exclude = ['fonia']

#################################################
class PinfControlloVarchiSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfControlloVarchi
    fields = '__all__'
