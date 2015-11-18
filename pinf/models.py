# coding: utf-8

from django.contrib.gis.db import models as geomodels
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


#################################################
class PinfTopoViario(models.Model):
  id = models.IntegerField(primary_key=True)
  nome = models.CharField(max_length=250, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_topo_viario'

#################################################
class PinfSosta(models.Model):
  id = models.IntegerField(primary_key=True)
  tipo = models.CharField(max_length=80)
  disposizione = models.CharField(max_length=80, blank=True, null=True)
  dove = models.CharField(max_length=80, blank=True, null=True)
  id_via = models.IntegerField(blank=True, null=True)
  posti = models.IntegerField(blank=True, null=True)
  
  class Meta:
    abstract = True

#################################################
class PinfSostaMultiLine(PinfSosta):
  geom = geomodels.MultiLineStringField(srid=4326, null=True, blank=True)
  objects = geomodels.GeoManager() # so we can use spatial queryset methods

  class Meta:
    abstract = True

#################################################
class PinfSostaPoint(PinfSosta):
  geom = geomodels.PointField(srid=4326, null=True, blank=True)
  objects = geomodels.GeoManager() # so we can use spatial queryset methods

  class Meta:
    abstract = True

#################################################
class PinfSostaGialloblu(PinfSostaMultiLine):
  pass

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_sosta_gialloblu'

### queryset e property a PinfTopoViario
u"""
Aggiunge a PinfTopoViario un queryset che contiene le istanze nella stessa strada.
"""
PinfTopoViario.sosta_gialloblu = property(lambda t: \
  PinfSostaGialloblu.objects.filter(id_via=t.id) or None)          
    
#################################################
class PinfSostaInvalidi(PinfSostaPoint):
  pass

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_sosta_invalidi'

### queryset e property a PinfTopoViario
u"""
Aggiunge a PinfTopoViario un queryset che contiene le istanze nella stessa strada.
"""
PinfTopoViario.sosta_invalidi = property(lambda t: \
  PinfSostaInvalidi.objects.filter(id_via=t.id) or None)          
    
#################################################
class PinfSostaMerci(PinfSostaPoint):
  pass

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_sosta_merci'

### queryset e property a PinfTopoViario
u"""
Aggiunge a PinfTopoViario un queryset che contiene le istanze nella stessa strada.
"""
PinfTopoViario.sosta_merci = property(lambda t: \
  PinfSostaMerci.objects.filter(id_via=t.id) or None)          
    
#################################################
class PinfSostaTuristici(PinfSostaPoint):
  orari = models.CharField(max_length=10, blank=True, null=True)
  euro_h = models.DecimalField(max_digits=38, decimal_places=34, blank=True, null=True)
  note = models.CharField(max_length=80, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_sosta_turistici'

### queryset e property a PinfTopoViario
u"""
Aggiunge a PinfTopoViario un queryset che contiene le istanze nella stessa strada.
"""
PinfTopoViario.sosta_turistici = property(lambda t: \
  PinfSostaTuristici.objects.filter(id_via=t.id) or None)          
    
