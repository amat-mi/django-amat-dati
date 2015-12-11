# coding: utf-8

from rest_framework import serializers

from pinf.models import PinfDisciplinaAree, PinfTopoViario, PinfTopoCiviciaree, \
  PinfSostaGialloblu, PinfSostaInvalidi, PinfSostaMerci, \
  PinfSostaTuristici, PinfControlloVarchi


#################################################
class PinfDisciplinaAreeSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfDisciplinaAree

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

#################################################
class PinfSostaGiallobluSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfSostaGialloblu

#################################################
class PinfSostaInvalidiSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfSostaInvalidi

#################################################
class PinfSostaMerciSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfSostaMerci

#################################################
class PinfSostaTuristiciSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfSostaTuristici

#################################################
class PinfControlloVarchiSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfControlloVarchi
