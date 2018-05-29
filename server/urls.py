# coding: utf-8

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path as url, include
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# Default login/logout views
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# OAuth2 provider
urlpatterns += [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]

urlpatterns += [
    url(r'^tweet/', include('tweet.urls', namespace='tweet')),
    # Questa è l'URL per la UI Client (in remoto gestita direttamente dal Web Server)
    url(r'^tweet/client/', RedirectView.as_view(url='/static/tweet/index.html', permanent=False), name="tweet-client"),    
]

urlpatterns += [
    url(r'^park/', include('park_server_core.urls', namespace='park')),
]

urlpatterns += [
    url(r'^pinf/', include('pinf.urls', namespace='pinf')),
]

urlpatterns += [
    url(r'^open/', include('open.urls', namespace='open')),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns += [
    url(r'^docs/', get_swagger_view(title='AMAT Dati API'))
]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
