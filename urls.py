from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import app.views
import api.urls

urlpatterns = patterns('',
    url(r'^api/$', include(api.urls)),
    
    url(r'^$', app.views.index, name='index'),


    # Uncomment the admin/doc linegit below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
