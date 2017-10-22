import requests

data = {
    'api_key':"d45fd466-51e2-4701-8da8-04351c872236",
    'api_secret':"171e8465-f548-401d-b63b-caf0dc28df5f",
    'img_uid' : "2bdcd1ad-47a6-45f8-ba74-86c765272422"
    }

r = requests.post('http://www.betafaceapi.com/service_json.svc/GetImageInfo', json = data)
b = r.json().get('faces')
def checkKeyValuePairExistence(dic, key, value):
        try:
            #print(dic[key])
            return dic[key] == value
        except KeyError:
            return False
def checkKeyValuePairExistence2(dic, key):
        try:
            for i in range(len(dic)):
                if (dic[i] == key):
                    print(dic[i])
                    return true
        except KeyError:
            return False

for dic in b[1]:
    print(b[1]['tags'])
    for e in b[1]['tags']:
        d = checkKeyValuePairExistence(e, "name", "eye color")
        print(d)
        print(e)
#c=checkKeyValuePairExistence2(b[1],"tags" )


    


