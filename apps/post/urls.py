from django.urls import path

from apps.post.views import hello, direction, test, about

urlpatterns = [
    path('hi/', hello),
    path('dir/', direction),
    path('test/', test),
    path('about/', about, name="about"),
]
