import json

from django.http import HttpResponse
from django.views.generic import View

from api.models import UserProfile

class AccessTokenView(View):
    def get(self, request, *args, **kwargs):
        # TODO get existing access token if not expired
        return HttpResponse('Hello, World!')

    def post(self, request, *args, **kwargs):
        # TODO expect social media outlet (facebook, linkedin, etc) and access token
        # TODO check for existing user profile
        # TODO for facebook, get extended access token and save that instead
        # TODO generate new access token that never expires
        return HttpResponse('Hello, World!')

class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        # TODO validate access token + retrieve user profile
        userProfile = UserProfile.objects.get(pk = kwargs.get('pk'))
        user = userProfile.user
        response = {
            'full_name': '%(first_name)s %(last_name)s' % user,
            'blurb': userProfile.blurb,
            'avatar': userProfile.avatar_url
        }
        return HttpResponse(json.dumps(response), mimetype="application/json")

class UserProfileListView(View):
    def get(self, request, *args, **kwargs):
        # TODO validate access token
        response = {
        }
        return HttpResponse(json.dumps(response), mimetype="application/json")
