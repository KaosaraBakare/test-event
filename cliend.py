import requests
import json
import uuid
url = "https://www.google-analytics.com/mp/collect?measurement_id=G-12TBLX9LCD&api_secret=CmzwujFrRcGObV4U9OsSp"
# url = 'https://www.google-analytics.com/debug/mp/collect?measurement_id=G-12TBLX9LCD&api_secret=CmzwujFrRcGObV4U9OsSp'
payload = {
  "client_id": str(uuid.uuid4()),
  # "non_personalized_ads": false,
  "events": 
  [
    {
        
      "name":"page-view",
      "params":{
      "category":"phone",
      "description":"water resistant",
        "name":"Samsung A13"
      # "debug_mode" : True
      
        }

    }
        ]
}
r = requests.post(url,data=json.dumps(payload),verify=True)
# if r.status_code == '200':
#   print("Event sent successfully")
# else :
#   print("not sent")

print(r.status_code)