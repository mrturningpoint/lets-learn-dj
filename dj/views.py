from django.shortcuts import render
from .models import chaivariety
from django.shortcuts import get_object_or_404
# Create your views here.
def all_chai(request):
    chais=chaivariety.objects.all()
    return render(request,'dj/work.html',{'chais':chais})

def desc(request,chai_id):
    chai= get_object_or_404(chaivariety,pk=chai_id)
    return render(request,'dj/detail.html',{'chai':chai})