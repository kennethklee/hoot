from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import Resource

from api.models import UserAccessToken

class AccessTokenResource(Resource):
  class Meta:
    resource_name = "token"
    list_allowed_methods = []
    detail_allowed_methods = ["get"]
    authentication = BasicAuthentication()

  def obj_get(self, request=None, **kwargs):
    # TODO refresh token
    access_token = UserAccessToken.objects.get_or_create(user=request.user)
    return access_token

  def obj_create(self, request=None, **kwargs):
    # TODO create user
    pass
