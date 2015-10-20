# coding: utf-8

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
#     url(r'^docs/', include('rest_framework_swagger.urls')),
)

urlpatterns += patterns('',
    url(r'^tweet/', include('tweet.urls')),
    # Questa è l'URL per la UI Client (in remoto gestita direttamente dal Web Server)
    url(r'^tweet/client/', RedirectView.as_view(url='/static/tweet/index.html', permanent=False), name="tweet-client"),    
)

urlpatterns += patterns('',
    url(r'^park/', include('park_server_core.urls')),
)

urlpatterns += patterns('',
    url(r'^pinf/', include('pinf.urls')),
)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
