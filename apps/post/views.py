from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def direction(request):
    return HttpResponse("Backend (Python/Django)")

def test(request):
    return render(request, 'test.html')

def about(request):
    context = {
        'title': "О нас",
        'description': "Мы группа 18-1B ",
        'students': ['Митаева Кызжибек', 'Нурпаяз кызы Арууке', 'Анвардинов Билолдин', 'Анапияев Залкар']
    }
    return render(request, 'about.html', context)