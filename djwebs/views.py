from django.shortcuts import render
from django.http import HttpResponse
from djwebs.models import Content
# Create your views here.
def init(request):
    return HttpResponse("sdfsa")

def index(request):
    import time
    import datetime
    list = Content.objects.all();
    return render(request, "index.html",{"list": list})



#def zip(reques
