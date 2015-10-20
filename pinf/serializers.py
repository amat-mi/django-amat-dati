# coding: utf-8

from rest_framework import serializers

from pinf.models import PinfSostaGialloblu, PinfSostaInvalidi, PinfSostaMerci, \
  PinfSostaTuristici


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
