import requests
import json

def emotion_detector(text_to_analyze):
    #Setting parameters for the request
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT = { "raw_document": { "text": text_to_analyze } }

    #Making the request
    response = requests.post(URL, json=INPUT, headers=HEADERS)

    #Formatting the request into usable JSON
    formattedResponse = json.loads(response.text)
    #Extracting only the emotion values
    emotions = formattedResponse['emotionPredictions'][0]['emotion']

    #Finding the highest emotion value and appending it as the dominant
    dominantEmotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominantEmotion

    #return emotions object
    return emotions
