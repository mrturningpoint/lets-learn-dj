from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("hey ,there it is the homepage of this site")
    return render(request,'index.html')
def about(request):
    return HttpResponse("hey ,there it is the aboutpage of this site")
def contact(request):
    return HttpResponse("hey ,there it is the contactpage of this site")



