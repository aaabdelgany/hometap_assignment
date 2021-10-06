import requests,os


def _septic_check(address,zipcode):
    url = "https://api.housecanary.com/v2/property/details?address&zipcode"
    hc_user = os.getenv('API_CHECK_SEPTIC__HOUSECANARY_USER', 'SET ME')
    hc_password = os.getenv('API_CHECK_SEPTIC__HOUSECANARY_PASSWORD', 'SET ME')

    headers = {  'content-type': 'application/json',
    'Cookie': 'hcid=7fab05d4623f49f68543599b33da6235'
    }
    params = {'address': address,
          'zipcode': zipcode}
    try:
        response = requests.request("GET", url,params=params, headers=headers,auth=(hc_user,hc_password))
        response=response.json()
    
    except requests.ConnectionError:
        return {"error":"Connection Error!"}
    
    try:
        septic_or_no = response["property/details"]["result"]["property"]["sewer"]
        return septic_or_no.lower()=="septic"
    except KeyError:
        return {"error":"there was an error"}
