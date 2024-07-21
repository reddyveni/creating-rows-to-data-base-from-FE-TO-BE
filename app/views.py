from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def insert_Topic(request):
    tn=input('enter topic')
    TTO=Topic.objects.get_or_create(topic_name=tn)
    bl=TTO[1]
    if bl:
        TO=TTO[0]
        TO.save()
        return HttpResponse('Topic is created')
    else:
        return HttpResponse ('Topic is already is present')
def  insert_Webpage(request):
    tn=input('enter topicname')
    QLTO=topic.objects.filter(topic_name=tn)
    if QLTO:
        TO=QLTO[0]
        na=input('enter name')
        url=input('enter url')
       
        WO=webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)
        WO=save()
        return HttpResponse('webpage is created')
    else:
        return HttpResponse('topic is not there si i cant created')

def insert_accessrecords(request):
    i=int(input('enter id:'))
    WO=Webpage.objects.filter(id=i)
    if WO:
        n=WO[0]
        a=input('enter author')
        d=input('enter u date')
        AO=Accessrecords.objects.get_or_create(name=n,auther=a,date=d)[0]
        AO.save()
        return HttpResponse('acessrecords is created')
    else:
        return HttpResponse('wo is query set of list')
def retrieve_topic(request):
    d={'topic':Topic.objects.all()}
    return render(request,'retrieving_topic.html',context=d)
def retrieve_Webpage(request):
    d={'webpage':Webpage.objects.all()}
def retrieve_accessrecords(request):
    d={'accessrecords':Accessrecords.objects.all()}
    return render(request,'retrieve_acessrecords.html',d)






