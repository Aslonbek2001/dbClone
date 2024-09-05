import requests
from django.core.files.base import ContentFile
from .models import QuizModel
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NTIzOTYwLCJpYXQiOjE3MjU1MjMzNjAsImp0aSI6ImE4YWI0OGY1ZmE3YzQ4MTRhMTM5NDk5YjhkNWY2N2FiIiwidXNlcl9pZCI6MX0.b1pcbiwIJ1ovZLpHE5QC8ygqdZWUXDZGP9KGiIwyp1U"
def send_quizzes_to_server():
    url = 'http://127.0.0.1:8001/quiz/create/'  # POST URLingizni kiritasiz
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}',  # Agar authorization kerak bo'lsa
    }

    quizzes = QuizModel.objects.all()
    
    for quiz in quizzes:
        # Yuborish uchun rasm fayllarini tayyorlash
        files = {}
        if quiz.foto:
            files['foto'] = (quiz.foto.name, quiz.foto.file, 'image/jpeg')
        if quiz.foto_answear:
            files['foto_answear'] = (quiz.foto_answear.name, quiz.foto_answear.file, 'image/jpeg')
        if quiz.foto_one:
            files['foto_one'] = (quiz.foto_one.name, quiz.foto_one.file, 'image/jpeg')
        if quiz.foto_two:
            files['foto_two'] = (quiz.foto_two.name, quiz.foto_two.file, 'image/jpeg')
        if quiz.foto_three:
            files['foto_three'] = (quiz.foto_three.name, quiz.foto_three.file, 'image/jpeg')
        
        # JSON formatida ma'lumotlar
        data = {
            'level': quiz.level,
            'number': quiz.number,
            'variant_size': quiz.vairant_size,
            'question': quiz.question,
            'sub_text': quiz.sub_text,
            'size': quiz.question_size,
            'answer': quiz.answer,
            'option_one': quiz.option_one,
            'option_two': quiz.option_two,
            'option_three': quiz.option_three,
        }
        
        response = requests.post(url, headers=headers, data=data, files=files)

        if response.status_code != 201:
            return False
    
    return True