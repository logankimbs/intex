import urllib.request
import json
import os
import ssl


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context


# this line is needed if you use self-signed certificate in your scoring service.
allowSelfSignedHttps(True)

# Request data goes here
data = {
    "Inputs": {
        "WebServiceInput1":
        [
            {
                'gender': "F",
                'state': "GA",
                'credentials': "NP",
                'specialty': "Nurse Practitioner",
                'isopioidprescriber': "TRUE",
                'totalprescriptions': "139",
                'atorvastatincalcium': "0",
                'avodart': "0",
                'diazepam': "0",
                'enalaprilmaleate': "0",
                'exelon': "0",
                'glimepiride': "0",
                'glipizideer': "0",
                'hydralazinehcl': "0",
                'klorconm20': "0",
                'levemir': "0",
                'levemirflexpen': "0",
                'metoclopramidehcl': "0",
                'namendaxr': "0",
                'nexium': "0",
                'nifedicalxl': "0",
                'nystatin': "0",
                'sucralfate': "0",
                'temazepam': "0",
                'tizanidinehcl': "0",
                'vesicare': "0",
            },
        ],
    },
    "GlobalParameters": {
    }
}

body = str.encode(json.dumps(data))

url = 'http://29fbe197-eaf7-4b30-a1a4-f6ca89592471.eastus2.azurecontainer.io/score'
# Replace this with the API key for the web service
api_key = 'lPOffRHFehD2gHoJAo56svmgZih4WPh8'
headers = {'Content-Type': 'application/json',
           'Authorization': ('Bearer ' + api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    result = json.loads(result)
    print("Total Prescriptions Prediction: " +
          str(round(float(result['Results']['WebServiceOutput0'][0]['Scored Labels']), 3)))

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
