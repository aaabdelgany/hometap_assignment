from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import _septic_check

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

@csrf_exempt
def septic_check(request):
    if request.method=="POST":
        body=json.loads(request.body)
        address=body["address"]
        zipcode=body["zipcode"]
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
            })