import logging
from django.core import serializers
import os
import string

from django.contrib.auth import authenticate, login
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, Http404, HttpResponse
from rest_framework.renderers import JSONRenderer

from .api.serializers import UserSerializer,PostDataSerializer
from .models import MyBackend, PostData

CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), '..', 'client_secrets.json')


def verify(request):
    if request.method == 'POST':
        rjson = json.loads(request.body.decode("utf-8"))
        # tokenId = request.POST.get('tokenId', 'nothing')
        #tokenId = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjczNGUxYzkyMmE4NWQwNDM2Njk1NTY4YjZmMzY2MzFhNmI1MzhkZmIifQ.eyJhenAiOiIxMDIwMjUxODAwNDY2LTdxdjg2ZWdvaGVkaHNyN2UwYWhtYzRqOTk4MWVha29kLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiMTAyMDI1MTgwMDQ2Ni1xdmNibzV1MjM0cDUxZGdtcmlrOWRjMGZ2azJmbW1qZC5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwODU0MDM3MDc2Mzg3NTU3MDgxNSIsImhkIjoiaWlpdGQuYWMuaW4iLCJlbWFpbCI6ImFuaWwxNjAwN0BpaWl0ZC5hYy5pbiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJpYXQiOjE1MDA4ODQwNzksImV4cCI6MTUwMDg4NzY3OSwibmFtZSI6IkFuaWwgQ2hvdWJleSIsInBpY3R1cmUiOiJodHRwczovL2xoNS5nb29nbGV1c2VyY29udGVudC5jb20vLTBJNVBDeTdFYnR3L0FBQUFBQUFBQUFJL0FBQUFBQUFBQUFBL0FNcDVWVW9nY0lJcERhZGRYN3dxb0hsZnlRc2xCYjFYQ0Evczk2LWMvcGhvdG8uanBnIiwiZ2l2ZW5fbmFtZSI6IkFuaWwiLCJmYW1pbHlfbmFtZSI6IkNob3ViZXkiLCJsb2NhbGUiOiJlbiJ9.wvA2-2d60R-c4bxZ5D941j-OrM7pByXyLBubntbByWSVT0oT8cfmj7u0Hh__bbZTAspOioJmjm9veAF7Y3sQR_hlWoF0HDv8jMV2QWOZwiGiNBSVk49EXC78A3HvnV3r12rCrOTo003yU0vq1GL-zLMr-MjwWqdQlm3wm2ZZZyBgkv2vMhPw3CN5C8ad5ntl684ohj3LOjxZDO46FyfuPuL_jE2u_0xYUI4T7XV4mTe1wj5IQhnHnxO4VQgYtrBSgmlc7izsAGX9LW_etXyBKDSPFX16BRC9UaRfFLgFoRbi6AShrYsQrrVbQ7_5kdkZMVE7lDfYvSFatxsiDT5FCw'
        tokenId = rjson['data']
        # return HttpResponse("{ \"result\" :\"" + tokenId + "\"}", content_type="application/json")
        user = MyBackend.authenticate(tokenId)
        if user is not None:
            if user.is_active:
                login(request, user)
                post_data = PostDataSerializer(PostData(user, 'ok'))
                response = HttpResponse("{ \"result\" :\"" + str(post_data.data)
 + "\"}",
                                        content_type="application/json")
            else:
                response = HttpResponse("{ \"result\" :\"" + "Disabled account" + "\"}",
                                        content_type="application/json")
        else:
            response = HttpResponse("{ \"result\" :\"" + "bad" + "\"}", content_type="application/json")

        return response
    else:
        tokenId = request.GET.get("tokenId", "nothing")
        # raise Http404("not got found ")
        response = HttpResponse("{ \"result\" :" + tokenId + " \"BAD\" }", content_type="application/json")
        return response
'''
def testttt(request):
    if request.method == 'POST':
        response = HttpResponse("{ \"result\" :" + request.user. + " \"BAD\" }", content_type="application/json")
        return response
'''