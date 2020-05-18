import requests
import json
import sys



IP_API = 'https://api.ipify.org'

API_KEY = 'PASTE GOOGLE API KEY HERE'

POST_URL = 'https://vision.googleapis.com/v1/images:annotate'

URLS = [line.rstrip('\n') for line in open('urls')]

ip_address = requests.get(IP_API).text

print(URLS)

i = 0
while i < len(URLS):
  print(URLS[i])
  resp = requests.post(
        'https://vision.googleapis.com/v1/images:annotate?key=' + API_KEY,
        json = {
          "requests": [{
            "image": {
              "source": {
			    "imageUri": URLS[i]
			    }
            },
            "features": [{
               "type": "LABEL_DETECTION",
              "maxResults": 3
            }]
          }]
        }
    )
  
  data = resp.json()
  
  print(data)
  
  try:
      
      json_data = data["responses"][0]["labelAnnotations"][0]["description"] + " " + data["responses"][0]["labelAnnotations"][1]["description"] + " " + data["responses"][0]["labelAnnotations"][2]["description"]
	  
  except:
    
      json_data = "An Error Occurreed"
  
  print(json_data)
  
  with open("alts", "a+") as file:
    file.write(URLS[i] + '\n' + 'Description: ' + json_data + '\n')

  i += 1