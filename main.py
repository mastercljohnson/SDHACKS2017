from flask import Flask, render_template, Response
from camera import use
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    y = str(use())
    form = {
    'api_key': 'd45fd466-51e2-4701-8da8-04351c872236',
    'api_secret': '171e8465-f548-401d-b63b-caf0dc28df5f',
    'detection_flags': 'propoints,classifiers,extended,bestface',
    'image_base64': y
    }
    data = {
        	"api_key":"d45fd466-51e2-4701-8da8-04351c872236",
	"api_secret":"171e8465-f548-401d-b63b-caf0dc28df5f",
	"detection_flags":"propoints%2classifiers%2extended%2bestface",
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
	"image_base64":y,
	"original_filename":"a.jpeg",
	"url":""
                }
    #r = requests.get('https://api.github.com/events')
    r = requests.post('http://www.betafaceapi.com/service_json.svc/UploadImage', json = data)
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
