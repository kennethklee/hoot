from django.http import HttpResponse
from django.views.generic import View

class AccessTokenView(View):
    def get(self, request, *args, **kwargs):
        # TODO get existing access token if not expired
        return HttpResponse('Hello, World!')

    def post(self, request, *args, **kwargs):
        # TODO generate new access token
        return HttpResponse('Hello, World!')
