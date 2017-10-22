from flask import Flask, render_template, Response
from camera import use
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    def checkKeyValuePairExistence(dic, key, value):
        try:
            return dic[key] == value
        except KeyError:
            return False
    y = str(use())
    data = {
	"api_key":"d45fd466-51e2-4701-8da8-04351c872236",
	"api_secret":"171e8465-f548-401d-b63b-caf0dc28df5f",
	"detection_flags":"cropface%2Crecognition%2Cclassifiers%2Cpropoints%2Cextended%2Cbestface",
	"image":[81,
	109,
	70,
	122,
	90,
	83,
	65,
	50,
	78,
	67,
	66,
	84,
	100,
	72,
	74,
	108,
	89,
	87,
	48,
	61],
	"image_base64":y[2:len(y)-1],
	"original_filename":"face.jpg",
	"url":""
}
    #r = requests.get('https://api.github.com/events')
    r = requests.post('http://www.betafaceapi.com/service_json.svc/UploadImage', json = data)
    a = r.json().get('img_uid')
    form = {
        "api_key":"d45fd466-51e2-4701-8da8-04351c872236",
	"api_secret":"171e8465-f548-401d-b63b-caf0dc28df5f",
        "img_uid" : a
        }

    r2 = requests.post('http://www.betafaceapi.com/service_json.svc/GetImageInfo', json = form)
    try :

        b = r2.json().get('faces')

        for e in b[0]['tags']:
            d = checkKeyValuePairExistence(e, "name", "color eyes")
            c = e
            if (d):
                wordlist = [
        #'red-wine-liking'
                #, 'smoking-behavior'
                #,'caffeine-metabolite-ratio'
                #,'endurance-performance'
                #,
                'eye-color'
                #,'red-hair'
                #, 'black-hair'
                #, 'skin-pigmentation'
                #,'freckles'
               # ,'openness'
        ]
                eyecolorbool = (c == "533f35")
                n=0
                reporteye = genomelink.Report.fetch(name='eye-color', population='european', token='6ProfWS0SNs4gTXmEAbrVBByQWyPhO')
                if (report.summary['score']> 2 & eyecolorbool):
                    return'genome prediction accurate'
                else :
                    return 'genome prediction inaccurate'
            else:
                return "cannot retrieve eye color data"


    #for trait in wordlist:
        #report = genomelink.Report.fetch(name=trait, population='european', token='6ProfWS0SNs4gTXmEAbrVBByQWyPhO')

        #print(report.summary['score'])
        #print(report.summary['text'])








    except :
        return 'no face found'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
