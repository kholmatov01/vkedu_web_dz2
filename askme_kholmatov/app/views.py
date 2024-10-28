from django.http import HttpResponse
from django.shortcuts import render

QUESTIONS = [
    {
        'title': 'title' + str(i),
        'id': i,
        'text': 'text' + str(i), 
    } for i in range(1,30)
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
    return render(request, template_name='hot.html', context={'questions': QUESTIONS})
def login(request):
    return render(request, template_name='login.html')
