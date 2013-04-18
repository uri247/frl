from django.conf.urls import patterns, url
from architect import views


urlpatterns = patterns( '',
    url( r'^$', views.index, name='index' ),
)
