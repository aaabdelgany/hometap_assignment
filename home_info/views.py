from django.shortcuts import render
from django.http import JsonResponse
from .utils import _septic_check



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
