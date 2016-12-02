from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from djwebs.models import Content


def add(request):
    return render(request, "add.html")


def hand(request):
    title   = request.POST["title"]
    content = request.POST['content']
    #b = request.POST("pass")
    import time
    import datetime
    dateC = datetime.datetime.now()
    timestamp = time.mktime(dateC.timetuple())
    contents = Content(title=title, content=content, time=timestamp)
    contents.save()


    # timestamp = 1372759811
    #
    # import time
    # print (time.strftime('%Y-%m-%d %X', time.localtime(timestamp)))
    #
    #
    #
    # print ("time to timestamp")
    #
    # import datetime
    # dateC = datetime.datetime.now()
    # timestamp = time.mktime(dateC.timetuple())
    # print ("python timestamp:", timestamp)

    return HttpResponseRedirect('/index/')
#def zip(reques
def delete(request):
    id = request.GET['id']
    Content.objects.filter(id=id).delete()
    return HttpResponseRedirect('/index/')

def update(request):
    id = request.GET['id']
    info = Content.objects.get(id=id)
    return render(request, "update.html", {"info":info})



def handupdate(request):
    title = request.POST["title"]
    content = request.POST['content']
    id = request.POST['id']

    #Content.objects.filter(title=title, content=content).update(id=id)
    k = Content.objects.get(id=id)

    k.title = title
    k.content = content

    k.save()
    return HttpResponseRedirect('/index/')
