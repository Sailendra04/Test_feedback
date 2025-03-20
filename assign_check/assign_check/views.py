from django.shortcuts import render
from .api import feedback
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def check(request):
    text = request.POST.get('text')
    output = feedback(text)
    # return render(request,'feed.html',{'text':output})
    return HttpResponse(output)