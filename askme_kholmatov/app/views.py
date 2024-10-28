import copy
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

QUESTIONS = [
    {
        'title': 'title' + str(i+1),
        'id': i,
        'text': 'text' + str(i+1),
        'tags': ['tag'+str(i*13%5+4), 'tag'+str(i*3%6), 'tag'+str(i*5%4)] 
    } for i in range(30)
]

# Create your views here.
def index(request):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(QUESTIONS, per_page=6)
    page = paginator.page(page_num)
    return render(
        request, template_name='index.html', 
        context={'questions': page.object_list, 'page_obj': page})

def ask(request):
    return render(request, template_name='ask.html')

def signup(request):
    return render(request, template_name='signup.html')

def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(hot_questions, per_page=6)
    page = paginator.page(page_num)
    return render(
        request, template_name='hot.html', 
        context={'questions': page.object_list, 'page_obj': page})

def tag(request, question_tag):
    tagged_questions = [q for q in QUESTIONS if question_tag in q['tags']]
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(tagged_questions, per_page=6)
    page = paginator.page(page_num)
    return render(request, template_name='tag.html', 
                  context={'questions': page.object_list, 'tag': question_tag, "page_obj": page})

def question(request, question_id):
    one_question = QUESTIONS[question_id]
    return render(request, template_name='question.html', context={'item': one_question})

def login(request):
    return render(request, template_name='login.html')

