# coding: utf-8

from django.contrib.gis import admin
from django.contrib.gis.geos.geometry import GEOSGeometry

from pinf.models import PinfSostaGialloblu, PinfSostaInvalidi, PinfSostaMerci, \
  PinfSostaTuristici


#################################################
class BaseAdmin(admin.ModelAdmin):
  save_on_top = True    

#################################################
class GMapsAdmin(admin.OSMGeoAdmin):
  save_on_top = True    
  map_width = 900
  map_height = 550
  g = GEOSGeometry('POINT (9.18963432972532 45.4642637335283)') # Set map center
  g.set_srid(4326)
  # see: https://code.djangoproject.com/ticket/22456  
#   g.transform(900913)
  g.transform(3857)
  default_lon = int(g.x)
  default_lat = int(g.y)
  default_zoom = 12           #zoom level if no point set
  point_zoom = 18             #zoom level if point set
#NOOO!!! Al 31/01/2014 la versione "dev" di OpenLayers non funziona!!!
#   openlayers_url = 'http://openlayers.org/dev/OpenLayers.js'
  openlayers_url = 'http://openlayers.org/api/2.13.1/OpenLayers.js'
  extra_js = ["http://maps.google.com/maps/api/js?v=3&sensor=false&region=IT&language=it"]
  map_template = 'gis/admin/gmaps.html'

#################################################
class PinfSostaGiallobluAdmin(GMapsAdmin):
  pass
admin.site.register(PinfSostaGialloblu,PinfSostaGiallobluAdmin)

#################################################
class PinfSostaInvalidiAdmin(GMapsAdmin):
  pass
admin.site.register(PinfSostaInvalidi,PinfSostaInvalidiAdmin)

#################################################
class PinfSostaMerciAdmin(GMapsAdmin):
  pass
admin.site.register(PinfSostaMerci,PinfSostaMerciAdmin)

#################################################
class PinfSostaTuristiciAdmin(GMapsAdmin):
  pass
admin.site.register(PinfSostaTuristici,PinfSostaTuristiciAdmin)
