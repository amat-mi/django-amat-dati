{% extends "gis/admin/openlayers.js" %}	
{% block base_layer %}
	//has base layer, use a plain Google Map
	new OpenLayers.Layer.Google("Google Mappa", {type: google.maps.MapTypeId.MAP});
{% endblock %}

{% block extra_layers %}

	//additional layers with Google Hybrid and OpenStreetMap
  {{ module }}.map.addLayer(new OpenLayers.Layer.Google("Google Ibrida", {type: google.maps.MapTypeId.HYBRID}));
	{{ module }}.map.addLayer(new OpenLayers.Layer.OSM("OpenStreetMap (Mapnik)"));
	
	//create a marker layer for goecoder results
	{{ module }}.layers.markers = new OpenLayers.Layer.Markers("Indirizzi trovati");
  {{ module }}.map.addLayer({{ module }}.layers.markers);

	//change the default style to make points more visually prominent
	OpenLayers.Feature.Vector.style["default"]["graphicName"] = "x";
	OpenLayers.Feature.Vector.style["default"]["strokeColor"] = "#ff0000";
	OpenLayers.Feature.Vector.style["default"]["strokeWidth"] = 3;
	OpenLayers.Feature.Vector.style["default"]["pointRadius"] = 9;	
	 
{% endblock %}

{% block controls %}
	{{ block.super }}
	
	var btnGeocoder = new OpenLayers.Control.Button({
    displayClass: "notused",
		title: "Cerca indirizzo", 
		trigger: function() {
			var address = [];
			address[0] = django.jQuery('#id_indirizzo').val();
			address[1] = django.jQuery('#id_civico').val();
			address[2] = django.jQuery('#id_cap').val();
			address[3] = django.jQuery('#id_citta').val();
			
			address = address.join(',');  
			var geocoder = new google.maps.Geocoder();
			geocoder.geocode({'address': address}, function(results,status) { 
				if (status == google.maps.GeocoderStatus.OK) {
					if (status != google.maps.GeocoderStatus.ZERO_RESULTS) {
						var coords = new OpenLayers.LonLat(results[0].geometry.location.lng(),results[0].geometry.location.lat())
							.transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")); 
						{{ module }}.map.setCenter(coords, 18);
						{{ module }}.layers.markers.addMarker(new OpenLayers.Marker(coords));
					}	
				}
				else {
					alert('Indirizzo non trovato: ' + address);
				}
			});  
		}
	});

	{{ module }}.panel.addControls([btnGeocoder]);

{% endblock controls %}
