# coding: utf-8

from rest_framework import serializers

from pinf.models import PinfTopoViario, PinfSostaGialloblu, PinfSostaInvalidi, PinfSostaMerci, \
  PinfSostaTuristici, PinfControlloVarchi


#################################################
class PinfTopoViarioSerializer(serializers.ModelSerializer):
  pass

  class Meta:
    model = PinfTopoViario
    fields = ['id','nome']

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
