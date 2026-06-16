import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=INPUT, headers=HEADERS)
    
    formattedResponse = json.loads(response.text)

    emotions = formattedResponse['emotionPredictions'][0]['emotion']

    dominantEmotion = max(emotions, key=emotions.get)
    print(dominantEmotion)
    emotions['dominant_emotion':dominantEmotion]

    return emotions