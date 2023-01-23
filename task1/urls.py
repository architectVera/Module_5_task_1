"""task1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http.request import HttpRequest;
from django.http.response import HttpResponse;


def lorem_ipsam(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Lorem ipsum dolor sit amet, consectetur adipiscing elit")


def progression(request: HttpRequest, start:int, count:int, step:int) -> HttpResponse:
    print(f"{start=}, {count=}, {step=}")
    l = [start]
    counter = 0
    while counter <= count:
        start = start + step
        counter += 1
        l.append(start)
    print(f"{l=}")
    return HttpResponse(" ".join(map(str,l)))


def fibonacci(n):
    if n <= 0:
        return "Incorrect input"
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def fb(request: HttpRequest, n: int) -> HttpResponse:
    return HttpResponse(str(fibonacci(n+1)))


def greeting(request: HttpRequest, name:int) -> HttpResponse:
    return HttpResponse(f"Greetign, {name}!")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("homepage/", lorem_ipsam),
    path('home/', lorem_ipsam),
    path('', lorem_ipsam),
    path('progression/<int:start>/<int:count>/<int:step>/', progression),
    path('fib/<int:n>/', fb),
    path('greeting/<str:name>/', greeting)
]

