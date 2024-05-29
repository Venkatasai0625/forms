from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
from app.models import *
def data_entry(request):
    ESFO=Student_data()
    d={'ESFO':ESFO}
     
    if request.method=='POST':
        SFDO=Student_data(request.POST)
        if SFDO.is_valid():
            print(SFDO.cleaned_data)
            #print(SFDO)
            return HttpResponse('Data Submitted')
        else:
            return HttpResponse("Data is invalid")
    return render(request,'data_entry.html',d)

def data_entry_topic(request):
    ETFO=TopicForm()
    d={"ETFO":ETFO}
    
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            topic_name=TFDO.cleaned_data['topic_name']
            print(topic_name)
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()

            #print(SFDO)
            return HttpResponse('Data Submitted')
        else:
            return HttpResponse("Data is invalid")
    return render(request,'data_entry_topic.html',d)



def data_entry_Webpage(request):
    EWFO=WebpageForm()
    d={"EWFO":EWFO}
    
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            topic_name=WFDO.cleaned_data['topic_name']
            name=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']
            email=WFDO.cleaned_data['email']
            TO=Topic.objects.get(topic_name=topic_name)
            WO=Topic.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
            WO.save()

            print(WFDO)
            return HttpResponse('Data Submitted')
        else:
            return HttpResponse("Data is invalid")
    return render(request,'data_entry_Webpage.html',d)

