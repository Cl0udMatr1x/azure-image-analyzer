# This code displays how to call the Azure Computer Vision Image Analyzer API from Python

# Use the requests library to simplify making a REST API call from Python 

import requests



# We will need the json library to read the data passed back 

# by the web service

import json



# You need to update the SUBSCRIPTION_KEY to 

# they key for your Computer Vision Service (Use Azure Keyvault for production)

SUBSCRIPTION_KEY = "d7130246aeb44ce18f76440a2d8875b6"



# Update the vision_service_address to the address of

# your Computer Vision Service

vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"



# Add the name of the function you want to call to the address

address = vision_service_address + "analyze"



# According to the documentation for the analyze image function 

# There are three optional parameters: language, details & visualFeatures

parameters  = {'visualFeatures':'Adult,Brands,Categories,Description,Color,Faces,ImageType,Objects,Tags',    
               'details':'Celebrities,Landmarks',
               'language':'en'}



# Open the image file to get a file object containing the image to analyze

image_path = r"C:\Users\User\Documents\Hello\PolarBear.jpg"

image_data = open(image_path, "rb").read()



# According to the documentation for the analyze image function

# we need to specify the subscription key and the content type

# in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly

headers    = {'Content-Type': 'application/octet-stream',

              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}



# According to the documentation for the analyze image function

# we use HTTP POST to call this function

response = requests.post(address, headers=headers, params=parameters, data=image_data)



# Raise an exception if the call returns an error code

response.raise_for_status()



# Display the JSON results returned

results = response.json()

print(json.dumps(results))