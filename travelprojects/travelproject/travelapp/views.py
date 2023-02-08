from django.shortcuts import render
from .models import Place,executives

def home(request):
    obj1=Place.objects.all()
    obj2=executives.objects.all()
    return render(request,'index.html',{'result1':obj1,'result2':obj2})
