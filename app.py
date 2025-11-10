from flask import Flask
import json

APP = Flask(__name__)

@APP.get("/info")
def info():
    return json.dumps([
        {
            'Integrantes':[
                'Renan Americo Herculano',
                'Leandro Pavan',
                'Lucas de Paula'
            ]
        }
    ])
