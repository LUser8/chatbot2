# importing the required model

from django.http import JsonResponse
from django.shortcuts import render
from .models import ChatAssistant


def bot_assistant(request):
    """ Function based view, extract record from the database and response back"""

    # Ajax call handling to response back on the fly
    if request.is_ajax():
        if request.method == 'POST':
            try:
                # extract the answer object for the selected question query
                answer_query = ChatAssistant.objects.get(question=request.POST['question'])

                # data to response back
                context = {
                    'answer': answer_query.answer
                }
            except ChatAssistant.DoesNotExist:
                # if the question is not in the database
                context = {
                    'answer': 'sorry, I didn\'t understand...'
                }
            return JsonResponse(context)    # json response for answers

        # ajax call handling to give the list of the questions when page load first time
        if request.method == 'GET':
            questions = []
            questions_obj = ChatAssistant.objects.all()
            for quest in questions_obj:
                questions.append(quest.question)

            # sending questions list in the response
            context = {
                'questions': questions
            }
            return JsonResponse(context)    # json response for questions list
    context = {
        'title': 'Assistant',
    }
    return render(request, 'bot/home.html', context)




