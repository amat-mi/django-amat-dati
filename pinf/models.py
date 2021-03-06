# coding: utf-8

from django.contrib.gis.db import models as geomodels
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


#################################################
class PinfDisciplinaAree(models.Model):
  id = models.IntegerField(primary_key=True)
  tipo = models.CharField(max_length=80, blank=True, null=True)
  nome = models.CharField(max_length=80, blank=True, null=True)
  ordinanza = models.CharField(max_length=200, blank=True, null=True)
  deroghe = models.TextField(blank=True, null=True)
  val_inizio = models.DateTimeField(blank=True, null=True)
  val_fine = models.DateTimeField(blank=True, null=True)
  geom = geomodels.MultiPolygonField(srid=4326, null=True, blank=True)
#   objects = geomodels.GeoManager() # so we can use spatial queryset methods

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_disciplina_aree'

#################################################
class PinfTopoViario(models.Model):
  id = models.IntegerField(primary_key=True)
  nome = models.CharField(max_length=250, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_topo_viario'

#################################################
class PinfTopoCiviciaree(models.Model):
  civico_id = models.IntegerField(primary_key=True)
  area_id = models.IntegerField(primary_key=True)
  tipo_rel = models.IntegerField(blank=True, null=True)
  note_rel = models.TextField(blank=True, null=True)
  tipo_area = models.CharField(max_length=80, blank=True, null=True)
  nome_area = models.CharField(max_length=80, blank=True, null=True)
  ordinanza = models.CharField(max_length=200, blank=True, null=True)
  val_inizio = models.DateTimeField(blank=True, null=True)
  val_fine = models.DateTimeField(blank=True, null=True)
  id_via = models.IntegerField(blank=True, null=True)
  numero = models.CharField(max_length=20, blank=True, null=True)
  geom = geomodels.PointField(srid=4326, null=True, blank=True)
#   objects = geomodels.GeoManager() # so we can use spatial queryset methods

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_topo_civiciaree'
    unique_together = (('civico_id', 'area_id'),)

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
class PinfSostaGialloblu(PinfSosta):
  geom = geomodels.MultiLineStringField(srid=4326, null=True, blank=True)
#   objects = geomodels.GeoManager() # so we can use spatial queryset methods

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_sosta_gialloblu'

### queryset e property a PinfTopoViario
u"""
Aggiunge a PinfTopoViario un queryset che contiene le istanze nella stessa strada.
"""
PinfTopoViario.sosta_gialloblu = property(lambda t: \
  PinfSostaGialloblu.objects.filter(id_via=t.id))          
    
#################################################
class PinfSostaInvalidi(PinfSosta):
  geom = geomodels.PointField(srid=4326, null=True, blank=True)
#   objects = geomodels.GeoManager() # so we can use spatial queryset methods

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_sosta_invalidi'

### queryset e property a PinfTopoViario
u"""
Aggiunge a PinfTopoViario un queryset che contiene le istanze nella stessa strada.
"""
PinfTopoViario.sosta_invalidi = property(lambda t: \
  PinfSostaInvalidi.objects.filter(id_via=t.id))          
    
#################################################
class PinfSostaMerci(PinfSosta):
  geom = geomodels.PointField(srid=4326, null=True, blank=True)
#   objects = geomodels.GeoManager() # so we can use spatial queryset methods

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_sosta_merci'

### queryset e property a PinfTopoViario
u"""
Aggiunge a PinfTopoViario un queryset che contiene le istanze nella stessa strada.
"""
PinfTopoViario.sosta_merci = property(lambda t: \
  PinfSostaMerci.objects.filter(id_via=t.id))          
    
#################################################
class PinfSostaTuristici(PinfSosta):
  orari = models.CharField(max_length=10, blank=True, null=True)
  euro_h = models.DecimalField(max_digits=38, decimal_places=34, blank=True, null=True)
  note = models.CharField(max_length=80, blank=True, null=True)
  geom = geomodels.PointField(srid=4326, null=True, blank=True)
#   objects = geomodels.GeoManager() # so we can use spatial queryset methods

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_sosta_turistici'

### queryset e property a PinfTopoViario
u"""
Aggiunge a PinfTopoViario un queryset che contiene le istanze nella stessa strada.
"""
PinfTopoViario.sosta_turistici = property(lambda t: \
  PinfSostaTuristici.objects.filter(id_via=t.id))          
    
#################################################
class PinfControlloPilomat(models.Model):
  id = models.IntegerField(primary_key=True)
  nome = models.CharField(max_length=80)
  indirizzo = models.CharField(max_length=80)
  id_via = models.IntegerField(blank=True, null=True)
  accesso = models.IntegerField()
  area_id = models.IntegerField(blank=True, null=True)
  tipo = models.CharField(max_length=16)
  fonia = models.CharField(max_length=40, blank=True, null=True)
  stato = models.IntegerField()
  note = models.TextField(blank=True, null=True)
  val_inizio = models.DateTimeField()
  val_fine = models.DateTimeField()
  geom = geomodels.PointField(srid=4326, null=True, blank=True)
#   objects = geomodels.GeoManager() # so we can use spatial queryset methods

  class Meta:
    managed = False
    db_table = 'pinf_new_amat_controllo_pilomat'

### queryset e property a PinfTopoViario
u"""
Aggiunge a PinfTopoViario un queryset che contiene le istanze nella stessa strada.
"""
PinfTopoViario.controllo_pilomat = property(lambda t: \
  PinfControlloPilomat.objects.filter(id_via=t.id))          
    
#################################################
class PinfControlloVarchi(models.Model):
  id = models.IntegerField(primary_key=True)
  tipo = models.CharField(max_length=80)
  dove = models.CharField(max_length=80, blank=True, null=True)
  id_via = models.IntegerField(blank=True, null=True)
  nome = models.CharField(max_length=80, blank=True, null=True)
  angolo = models.IntegerField(blank=True, null=True)
  area_id = models.IntegerField(blank=True, null=True)
  tipo_area = models.CharField(max_length=80, blank=True, null=True)
  accesso = models.NullBooleanField()
  geom = geomodels.PointField(srid=4326, null=True, blank=True)
#   objects = geomodels.GeoManager() # so we can use spatial queryset methods
  
  class Meta:
    managed = False
    db_table = 'pinf_new_amat_controllo_varchi'

### queryset e property a PinfTopoViario
u"""
Aggiunge a PinfTopoViario un queryset che contiene le istanze nella stessa strada.
"""
PinfTopoViario.controllo_varchi = property(lambda t: \
  PinfControlloVarchi.objects.filter(id_via=t.id))          
