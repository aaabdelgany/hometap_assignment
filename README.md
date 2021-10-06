Septic_Check API Endpoint:
This basic web app sets up an API endpoint to check whether a house at a given address has a septic tank or not. The Address and Zipcode of the house is passed to the endpoint as URL parameters. The request will then hit an external API with that address and zipcode to get a response JSON object that contains information about the house - including it's sewage type. The utility functionparses the response from the external API to get the sewage type and send a boolean value that depends on whether the house has septic sewage or not.

Failed requests to the external API due to connection issues or invalid authentication are handled and an error object is sent to the initial requester with a status code that is appropriate for the underlying issue.

A Mock Postman server was set up to simulate a successful response to House Canary's property/details API endpoint. This was set up to test the parsing of a standard response from that endpoint due to a lack of valid credentials for HC's API.

How To Run And Test This Project:

1. Clone this repo
2. Create a virtual environment: 'python -m venv venv' and activate it: 'source venv/bin/activate'
3. Install all dependencies: pip install requirements.txt
4. Run all migrations(not strictly necessary) python3 manage.py migrat
5. Run tests via the following command: python ./manage.py test
6. Set up HouseCanary authentication by setting the environment variables below
   export HC_API_KEY="KEY"
   export HC_API_SECRET="SECRET"
7. Run the server via the following command: python ./manage.py runserver
8. Send a GET request via postman or any other request tool to the below URL and observe the response (Please adjust the port in the url if you started the server on a different port):
   localhost:8000/home_info/septic_check?address=1234test Dr&zipcode=02048
