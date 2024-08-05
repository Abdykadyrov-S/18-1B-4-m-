from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def main(request):
#     return HttpResponse("Главная страница")

def index(request):
    context = {
        'title': "Главная",
        'description': "Описание главной страницы",
    }
    return render(request, 'index.html', context)