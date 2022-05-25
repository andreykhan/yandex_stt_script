import requests

API_KEY = "AQVN0RC-Sn8nnMaNvJMGZQNOmXvthz1SSNd4aiMM"
URL = 'https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize'
headers = {
    'Accept': 'application/json',
    'Authorization': f'Api-Key {API_KEY}'
}

data = {
    "config": {
        "specification": {
            "languageCode": "ru-RU",
            "model": "general",
            "profanityFilter": "false",
            "audioEncoding": "MP3",
            "sampleRateHertz": "48000",
            "audioChannelCount": "1"
        }
    },
    "audio": {
        "uri": "https://storage.yandexcloud.net/andreykhanbacket/2021-12-23_17-49_77089494952_incoming.mp3"
    }
}


def push_audio():
    req = requests.post(URL, headers=headers, json=data)
    print(req)
    print(req.text)
    operationId = req.json()['id']
    print(operationId)


def get_result():
    result = requests.get('https://operation.api.cloud.yandex.net/operations/e03ohorfc4c3i4cefldi', headers=headers)
    print(result)
    #print(result.json())
    print(result.json()['response']['chunks'])


#push_audio()
get_result()