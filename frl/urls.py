from django.conf.urls import patterns, include, url
from django.contrib import admin
import architect

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(architect.urls)),
)
