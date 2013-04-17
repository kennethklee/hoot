from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api import resources
from api import views

v1_api = Api(api_name='v1')
v1_api.register(resources.AccessTokenResource())

urlpatterns = patterns('',
    # Insert into v1 api
    url(r'^v1/access/?$', views.AccessTokenView.as_view()),
    url(r'^v1/profiles/?$', views.UserProfileListView.as_view()),
    url(r'^v1/profiles/(?P<pk>\d+)/?$', views.UserProfileView.as_view()),

    #url(r'', include(v1_api.urls)),
)
