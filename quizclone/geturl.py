import requests
from .models import QuizModel
from django.core.files.base import ContentFile
from urllib.parse import urlsplit

def download_image(image_url):
    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            filename = urlsplit(image_url).path.split('/')[-1]  # Extract filename from URL
            return ContentFile(response.content, name=filename)
    return None


def get_url():
    url = 'https://aslondev.uz/quiz/level/1/'
    headers = {
        'accept': 'application/json',
        # 'Authorization': 'Bearer ThX-uF0cU2A2tmxyoJtnqxc9Pv-m5prT'  # Uncomment this if authorization is needed
    }

    params = {
        # 'type': 'all',  # Uncomment or modify as needed
        # 'limit': 200,   # Uncomment or modify as needed
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            quiz, created = QuizModel.objects.get_or_create(
                id=item['id'],  # Use unique fields to check if it exists
                defaults={
                    'level': item.get('level'),
                    'number': item.get('number'),
                    'vairant_size': item.get('variant_size'),
                    'question': item.get('question', ''),
                    'sub_text': item.get('sub_text', ''),
                    'foto': item.get('foto'),
                    'question_size': item.get('size'),
                    'answer': item.get('answer'),
                    'foto_answear': item.get('foto_answear'),
                    'option_one': item.get('option_one'),
                    'foto_one': item.get('foto_one'),
                    'option_two': item.get('option_two'),
                    'foto_two': item.get('foto_two'),
                    'option_three': item.get('option_three'),
                    'foto_three': item.get('foto_three'),
                }
            )
            if item.get('foto'):
                quiz.foto.save(item['foto'].split('/')[-1], download_image(item['foto']))
            if item.get('foto_answear'):
                quiz.foto_answer.save(item['foto_answear'].split('/')[-1], download_image(item['foto_answear']))
            if item.get('foto_one'):
                quiz.foto_one.save(item['foto_one'].split('/')[-1], download_image(item['foto_one']))
            if item.get('foto_two'):
                quiz.foto_two.save(item['foto_two'].split('/')[-1], download_image(item['foto_two']))
            if item.get('foto_three'):
                quiz.foto_three.save(item['foto_three'].split('/')[-1], download_image(item['foto_three']))
        
        return "Data saved successfully!"
    else:
        return f"Xatolik yuz berdi: {response.status_code}"

