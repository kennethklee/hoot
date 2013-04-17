from tastypie.authentication import Authentication, BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import Resource

from api.models import UserAccessToken

class AccessTokenResource(Resource):
    class Meta:
        queryset = UserAccessToken.objects.all()
        resource_name = "token"
        include_resource_uri = False
        fields = ["access_token", "expires"]
        list_allowed_methods = []
        detail_allowed_methods = ["get"]
        authentication = Authentication()
        #authentication = BasicAuthentication()

