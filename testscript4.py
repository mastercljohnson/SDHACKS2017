import requests
data = {
    "api_key":"d45fd466-51e2-4701-8da8-04351c872236",
	"api_secret":"171e8465-f548-401d-b63b-caf0dc28df5f",
    'img_uid':'d7c897dd-b946-4ef4-a170-8fcc4ffc6a11'
    }
r = requests.post('http://www.betafaceapi.com/service_json.svc/UploadImage', json = data)
print(r.text)
