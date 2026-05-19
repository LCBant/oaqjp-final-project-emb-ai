import requests

def emotion_detector(text_to_analyze):

    response = requests.post('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
    json= {"raw_document": { "text": text_to_analyze }})
    data = response.json()

    text = data['emotionPredictions'][0]['emotionMentions'][0]['span']['text']

    emotions_dict = {
    'anger': data['emotionPredictions'][0]['emotion']['anger'],
    'disgust': data['emotionPredictions'][0]['emotion']['disgust'],
    'fear': data['emotionPredictions'][0]['emotion']['fear'],
    'joy': data['emotionPredictions'][0]['emotion']['joy'],
    'sadness': data['emotionPredictions'][0]['emotion']['sadness'],
    }
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    emotions_dict['dominant_emotion'] = dominant_emotion

    return emotions_dict
