from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic inserted successfully')
def insert_webpage(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name='tn')[0]
    TO.save() 
    n=input('enter name')
    url=input('enter url:')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]  
    WO.save()
    return HttpResponse('webpage is inserted successfully')
def insert_AcessRecord(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save() 
    n=input('enter name')
    url=input('enter url:')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]  
    WO.save()
    name=input('enter a name')
    author=input('enetr a author')
    date=input('enetr a date')
    AO=AcessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
    AO.save()
    return HttpResponse('AcessRecord inserted successfully')