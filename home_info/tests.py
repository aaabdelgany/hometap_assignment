import requests,json
from django.urls import reverse
from django.test import TestCase,Client


#The below object is taken from the housecanary documentation and is the example response that the postman mock server 
#will return
# housecanary_resp={
#     "property/details": {
#         "api_code_description": "ok",
#         "api_code": 0,
#         "result": {
#             "property": {
#                 "air_conditioning": "yes",
#                 "attic": False,
#                 "basement": "full_basement",
#                 "building_area_sq_ft": 1824,
#                 "building_condition_score": 5,
#                 "building_quality_score": 3,
#                 "construction_type": "Wood",
#                 "exterior_walls": "wood_siding",
#                 "fireplace": False,
#                 "full_bath_count": 2,
#                 "garage_parking_of_cars": 1,
#                 "garage_type_parking": "underground_basement",
#                 "heating": "forced_air_unit",
#                 "heating_fuel_type": "gas",
#                 "no_of_buildings": 1,
#                 "no_of_stories": 2,
#                 "number_of_bedrooms": 4,
#                 "number_of_units": 1,
#                 "partial_bath_count": 1,
#                 "pool": True,
#                 "property_type": "Single Family Residential",
#                 "roof_cover": "Asphalt",
#                 "roof_type": "Wood truss",
#                 "site_area_acres": 0.119,
#                 "style": "colonial",
#                 "total_bath_count": 2.5,
#                 "total_number_of_rooms": 7,
#                 "sewer": "municipal",
#                 "subdivision" : "CITY LAND ASSOCIATION",
#                 "water": "municipal",
#                 "year_built": 1957,
#                 "zoning": "RH1"
#             },

#             "assessment":{
#                 "apn": "0000 -1111",
#                 "assessment_year": 2015,
#                 "tax_year": 2015,
#                 "total_assessed_value": 1300000.0,
#                 "tax_amount": 15199.86
#             }
#         }
#     }
# }
client = Client()

class Tests(TestCase):
    
    def test_1(self):
        #test to postman mock server to verify that the request completed
        testUrl='https://5a2845d9-4cf3-4c6c-936f-9ead65ac8060.mock.pstmn.io/home_info/septic_check?address=1+test+way&zipcode=02048'
        resp=requests.request("GET",testUrl)
        self.assertEqual(resp.status_code,200)
    def test_2(self):
        #test to postman mock server to verify that the logic for parsing the response is correct. 
        testUrl='https://5a2845d9-4cf3-4c6c-936f-9ead65ac8060.mock.pstmn.io/home_info/septic_check?address=1+test+way&zipcode=02048'
        resp=requests.request("GET",testUrl).json()
        septic_or_no = resp["property/details"]["result"]["property"]["sewer"]
        self.assertFalse(septic_or_no.lower()=='septic')
    def test_3(self):
        #test to local septic_check route with the right HTTP method, the request will fail because the util is missing the necessary
        #credentials
        url=reverse('septic_check')
        url+="?address=1234test Dr&zipcode=02048"
        resp = client.get(url)
        self.assertEqual(resp.status_code,500)
    def test_4(self):
        #test to the local septic_check route with the wrong HTTP method,  to verify that the status code is 405, forbidden
        testBody={"address":"1 test way","zipcode": "02048"}
        url=reverse('septic_check')
        resp = client.post(url,data=json.dumps(testBody),content_type='application/json')
        self.assertEqual(resp.status_code,405)

