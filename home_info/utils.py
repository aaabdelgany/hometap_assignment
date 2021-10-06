import requests,os


def _septic_check(address,zipcode):
    url = "https://api.housecanary.com/v2/property/details?"
    hc_key = os.getenv('HC_API_KEY', '')
    hc_secret = os.getenv('HC_API_SECRET', '')
    #The House Canary documentation states that the api key is used as a username and the api secret is the pw
    headers = {  'content-type': 'application/json',
    'Cookie': 'hcid=7fab05d4623f49f68543599b33da6235'
    }
    params = {'address': address,
          'zipcode': zipcode}
    try:
        response = requests.request("GET", url,params=params, headers=headers,auth=(hc_key,hc_secret))
        response=response.json()
    
    except requests.ConnectionError:
        #error handling in case the request fails
        return {"error":"Connection Error!"}
    
    try:
        #parse the response to see if there is a response object that matches what we are looking for.
        #if we run into a key error because the response object is missing that key, then we know
        #that the request didn't return what we're looking for.
        #ex: a request to HC without the right creds returns the following object:
        #{"message": "Invalid credentials"}

        septic_or_no = response["property/details"]["result"]["property"]["sewer"]
        return septic_or_no.lower()=="septic"
    except KeyError:
        return {"error":"error"}
