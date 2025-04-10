from django.shortcuts import render

# Create your views here.
def printf(request):
    return render(request,'dj/work.html')
