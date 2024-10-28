import copy
from django.http import HttpResponse
from django.shortcuts import render

QUESTIONS = [
    {
        'title': 'title' + str(i+1),
        'id': i,
        'text': 'text' + str(i+1), 
    } for i in range(30)
]

# Create your views here.
def index(request):
    return render(
        request, template_name='index.html', context={'questions': QUESTIONS})
def ask(request):
    return render(request, template_name='ask.html')
def signup(request):
    return render(request, template_name='signup.html')
def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    return render(request, template_name='hot.html', context={'questions': hot_questions})
def question(request, question_id):
    one_question = QUESTIONS[question_id]
    return render(request, template_name='question.html', context={'item': one_question})
def login(request):
    return render(request, template_name='login.html')

