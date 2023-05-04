from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from valiface.models import *
import cv2
from ML import predict_face
import numpy as np
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.decorators.csrf import csrf_exempt
import cv2 as cv

# Create your views here.

BASE_DIR = getattr(settings, 'BASE_DIR')

def create_user(request):
    if request.method == 'POST':
        if(int(request.POST['perm']) == 0):
            func = Funcionario(nome_func=request.POST['nome'],
                            cargo_func=request.POST['cargo'],
                            foto_func=request.FILES.get('foto', None))
            func.save()
        else:
            pass
    return HttpResponse("Funcionário cadastrado")
    
def teste(request):
    return render(request,
                  'base.html',
                  content_type='text/html')
@csrf_exempt
def predict_img(request):
    response=JsonResponse({"id":-1,"nome":None,
                           "cargo":None,"confiança":0.0})
    img:InMemoryUploadedFile = request.FILES.get("img",None)
    if str(request.method) == "POST" and img is not None:
        image=cv2.imdecode(np.frombuffer(img.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        label, confidence = predict_face.predict(image)
        if(label!=-1):
            #Recupera o funcionário
            func:Funcionario=Funcionario.objects.get(pk=label)
            if(func!=None):
                response["id"]=func.pk
                response["nome"]=func.nome_func
                response["cargo"]=func.cargo_func
        response["confiança"]=confidence
    else:
        print("Não encontrou no banco")
    
    return response