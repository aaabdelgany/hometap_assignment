from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from .utils import _septic_check



#The below decorator was added to ensure that the csrf cookie would be set. This decision was
# made in case the front end was a react app where any form may be dynamically generated
# as opposed to a traditional template. Django may not set the csrf cookie on such pages.
# The react app will need to grab the csrf cookie and add it to the header of the post 
# request 
# @ensure_csrf_cookie
def septic_check(request):
    if request.method=="GET":
        address=request.GET.get('address')
        zipcode=request.GET.get('zipcode')
        if not (address and zipcode):
            return JsonResponse(
                { "error":"Missing Parameter!"},
                status=400)
        septic=_septic_check(address,zipcode)
        if type(septic)=='boolean':
            return JsonResponse({
                "septic":septic
            })
            
        else:
            return JsonResponse({
                "error":"There was an error while processing your request."
            },status=500)
    else:
        #if request.method is not GET
        return JsonResponse({
            "error": "Method not allowed"
        },status=405)
