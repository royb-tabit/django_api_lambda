from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
def ping(request):
    return HttpResponse("Were you expecting a Pong?")
