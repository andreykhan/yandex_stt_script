import requests
import os
import time
import pathlib

results = tuple()
API_KEY = "AQVN0RC-Sn8nnMaNvJMGZQNOmXvthz1SSNd4aiMM"
POST_URL = 'https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize'
GET_URL = 'https://operation.api.cloud.yandex.net/operations/'
headers = {
        'Accept': 'application/json',
        'Authorization': f'Api-Key {API_KEY}'
    }
for audio_name in os.listdir(path='C:\dev\calls_test'):
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
            "uri": 'https://storage.yandexcloud.net/andreykhanbacket/'+audio_name
        }
    }

    req = requests.post(POST_URL, headers=headers, json=data)
    print((req.json()['id']))
    print(f"{audio_name} was successfully submitted for transcription")
    results = results + ((req.json()['id']),)
    print(results)


for audio_id in results:
    while requests.get(GET_URL+audio_id, headers=headers).json()['done'] \
            is False:
        time.sleep(1)
    result_req = requests.get('https://operation.api.cloud.yandex.net/operations/'+audio_id, headers=headers)
    y = (result_req.json()['response']['chunks'][0]['alternatives'][0]['text'])
    print(y)
    with open(pathlib.Path('C:/') / 'dev' / 'call_results' / 'results.txt', 'a', encoding="utf-8") as f:
        f.write(y)
        f.write("\n")
    f.close()
