from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

def some_page(request):
    return HttpResponse("this is Some_page :D") 