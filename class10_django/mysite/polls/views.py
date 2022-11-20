from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Polls Application Page</h1>")

def about(request):
    return HttpResponse("<h2>Pakistan zinda bad!</h2>")