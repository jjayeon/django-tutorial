from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world and all who inhabit it")
