from django.shortcuts import render
from kubernetes import client, config, watch
import subprocess as sp
import os




def index(request):
    
    return render(request, 'KubrnetesCrud/index.html')

def contextname(request):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    w = watch.Watch()
    a1=[]
    for event in w.stream(v1.list_namespace, timeout_seconds=1):
        a1.append(event['object'].metadata.name)
    context = { 
        "data" : a1, 
    }
    return render(request, 'KubrnetesCrud/namespaces.html',context)


def getcontexts(request):
    contexts, active_context = config.list_kube_config_contexts()
    currentcon=[]
    currentcon.append(active_context)
    context1 = { 
        "data" : contexts,
        "data1" : currentcon, 
    }
    return render(request, 'KubrnetesCrud/getcontext.html',context1)

def changecontexts(request):
    if request.method == "GET":
        user=request.GET['contexts']
        command='kubectl config use-context '+user
        os.system(command)
    context={
        "data" : True,
        "contexts" : user,
    }
    return render(request, 'KubrnetesCrud/index.html',context)



    
 