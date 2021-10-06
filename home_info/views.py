from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import _septic_check


def index(request):
    return HttpResponse("Hello, world!")

@csrf_exempt #The decision was made to make this endpoint csrf_exempt because the front end application would be done in react and post to this endpoint directly as opposed to using django forms. If this goes live, I would change it to ensure_csrf_cookie and get the token from the cookies and add it as a header
def septic_check(request):
    if request.method=="POST":
        body=json.loads(request.body)
        address=body["address"]
        zipcode=body["zipcode"]
        print(address, zipcode)
        if not (address and zipcode):
            return JsonResponse({
                "error":"Missing address and/or Zipcode!"
            })
        septic=_septic_check(address,zipcode)
        if type(septic)=='boolean':
            return JsonResponse({
                "septic":septic
            })
            
        else:
            return JsonResponse({
                "error":"There was an error while processing your request. Please try again later"
            },status=500)
    else:
        return JsonResponse({
            "error": "Method not allowed"
        },status=405)