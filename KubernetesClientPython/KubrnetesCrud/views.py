from django.shortcuts import render
from kubernetes import client, config, watch
import subprocess as sp
import os



config.load_kube_config()

def index(request):
    try:
        os.system("kubectl get ns")
        msg=""
    except Exception :
        msg="Please start your cluster first"
    context = {
        "data" : msg
    }
    return render(request, 'KubrnetesCrud/index.html',context)

def contextname(request):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    w = watch.Watch()
    a1=[]
    for event in w.stream(v1.list_namespace, timeout_seconds=1):
        a1.append(event['object'].metadata.name)
    a1.sort()
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

def listpodinnamespace(request):
    if request.method == "GET":
        ns=request.GET['ns']
    v1 = client.CoreV1Api()
    a1=[]
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        if i.metadata.namespace==ns:
            a1.append([i.status.pod_ip,i.metadata.namespace,i.metadata.name,i.status.phase,i.status.container_statuses[0].restart_count])
    context={
        "data" : a1
    }
    return render(request, 'KubrnetesCrud/pods.html',context)

def getpoddetail(request):
    if request.method == "GET":
        describe=request.GET['describe']
        log=request.GET['log']
        podname=request.GET['podname']
        ns=request.GET['ns']

        if log=="View":
            api_instance = client.CoreV1Api()
            api_response = api_instance.read_namespaced_pod_log(name=podname, namespace=ns)
        if describe=="View":
            os.system("kubectl describe pod"+podname+" -n"+ns+">pdescribe")
            a=os.system("echo pdescribe")
            print(a)

    return render(request, 'KubrnetesCrud/log-describe.html')
    
       

    
 
