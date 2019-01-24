from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import ChatAssistent



def home(request):
    if request.is_ajax():
        if request.method == 'POST':
            # print(request.POST)
            answer_query = ChatAssistent.objects.get(question=request.POST['question'])
            context = {
                'answer': answer_query.answer
            }
            return JsonResponse(context)
        if request.method == 'GET':
            questions = []
            questions_obj = ChatAssistent.objects.all()
            for quest in questions_obj:
                questions.append(quest.question)
            context = {
                'questions': questions
            }
            return JsonResponse(context)
    context = {
        'title': 'Home',
    }
    return render(request, 'bot/home2.html', context)


