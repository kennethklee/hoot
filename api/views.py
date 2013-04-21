import json
import time

from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.models import User

from facepy import get_extended_access_token, GraphAPI

from api.models import UserProfile, UserAccessToken

class AccessTokenView(View):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        api_type = body.get('type', None)
        email = None
        # expect social media outlet (facebook, linkedin, etc) and access token
        if (api_type == 'facebook'):
            # TODO for facebook, get extended access token and save that instead
            access_token, expires_at = get_extended_access_token(body.get('access_token', None), settings.FACEBOOK_APP_ID, settings.FACEBOOK_API_SECRET)
            graph = GraphAPI(access_token)
            api_user = graph.get('/me')
            # TODO check for existing user profile
            try:
                user = User.objects.get(email = api_user.get('email', None))
                is_new = False
            except User.DoesNotExist:
                is_new = True
                print 'new user {0}'.format(api_user.get('email'))
                arg_user = {
                    'email': api_user.get('email'),
                    'username': api_user.get('email'),
                    'first_name': api_user.get('first_name'),
                    'last_name': api_user.get('last_name'),
                    'password': None
                }
                #user = User.objects.create_user(api_user.get('email'), api_user.get('email'), None)
                user = User.objects.create_user(**arg_user)

            user.first_name = api_user.get('first_name')
            user.last_name = api_user.get('last_name')
            user.save()

            profile = user.profile
            profile.avatar_url = 'http://graph.facebook.com/{0}/picture'.format(api_user.get('id'))
            profile.blurb = api_user.get('quotes', None)
            profile.save()

            # TODO generate access token or get existing
            arg_access_token = {
                'access_token': access_token, # TODO don't use facebook's access token
                'expires': time.mktime(expires_at.timetuple())  # TODO don't use facebook's expiry
            }
            try:
                user_access_token = UserAccessToken.objects.get(user = user)
                is_new_access_token = False
            except UserAccessToken.DoesNotExist:
                user_access_token = UserAccessToken.objects.create(user = user, **arg_access_token)
                is_new_access_token = True
                
            # TODO update access token
            print 'user {0} exists'.format(user.email)
        else:
            return HttpResponse('{}', mimetype="application/json")
            
        response = {
            'access_token': user_access_token.access_token,
            'expires': user_access_token.expires,
            'user': {
                'is_new': is_new,
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'avatar_url': profile.avatar_url,
                'blurb': profile.blurb
            }
        }
        return HttpResponse(json.dumps(response), mimetype="application/json")


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        if (UserAccessToken.is_valid(request.GET.get('access_token', None))):
            # TODO validate access token + retrieve user profile
            profile = UserProfile.objects.get(pk = kwargs.get('pk'))
            user = profile.user
            response = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'blurb': profile.blurb,
                'avatar': profile.avatar_url
            }
            return HttpResponse(json.dumps(response), mimetype="application/json")


class UserProfileListView(View):
    def get(self, request, *args, **kwargs):
        # TODO validate access token
        response = {
        }
        return HttpResponse(json.dumps(response), mimetype="application/json")
