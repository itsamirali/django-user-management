from django.http import HttpResponse

# Create your views here.


def home(request):
    method = request.method
    return HttpResponse("the request method is " + method)
