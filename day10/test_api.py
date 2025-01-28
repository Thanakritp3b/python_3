import requests

airq_api_url = "https://api.waqi.info/feed/#city#/?token=25feed2475f6b38f1079df22af8826ffbff4f58e"

request_url = airq_api_url.replace("#city#", "Bangkok")

request = requests.get(request_url)
json_data = request.json()['data']

print(f"{json_data['city']['name']} has airpollusion {json_data['iaqi']['pm25']}")
