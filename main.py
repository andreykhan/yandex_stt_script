import requests
from requests.auth import HTTPBasicAuth
import os

API_KEY="AQVN1uK7XHxgyMOZC2dHbKq2FpNS0X3fza1mMREy"
URL = 'https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize'
headers = {
    'Accept': 'application/json',
    'Api-Key': API_KEY
}
auth = HTTPBasicAuth('apikey', 'AQVN1uK7XHxgyMOZC2dHbKq2FpNS0X3fza1mMREy')
#auth = {"apikey": "API_KEY"}
data = {
    "config": {
        "specification": {
            "languageCode": "ru-RU",
            "model": "general",
            "profanityFilter": "false",
            "audioEncoding": "LINEAR16_PCM",
            "sampleRateHertz": "48000",
            "audioChannelCount": "5"
        }
    },
    "audio": {
        "uri": "https://storage.yandexcloud.net/andreykhanbacket/2021-02-19_17-33_77084597488_incoming.mp3"
    }
}


def push_audio():
    req = requests.post(URL, headers=headers, auth=auth, json=data)
    print(req)
    print(req.text)

push_audio()
