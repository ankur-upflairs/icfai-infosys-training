from django.http import HttpResponse


def about(request):
    return HttpResponse('<h1>this is about page</h1>')

def blogs(request):
    return HttpResponse('this is blog post')
def home(request):
    return HttpResponse('this is home page')
