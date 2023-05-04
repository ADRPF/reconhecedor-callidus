from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from valiface.models import *
from PIL import Image
from django.core.handlers.wsgi import WSGIRequest
import numpy as np
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.decorators.csrf import csrf_exempt
from ML.predict_face import predict

# Create your views here.


def create_user(request):
    if request.method == 'POST':
        if (int(request.POST['perm']) == 0):
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
def predict_img(request: WSGIRequest):
    # ver se o método é o POST e se tem alguma imagem
    response=JsonResponse({"id":-1,"nome":None,"cargo":None,"confiança":0.0})
    imagem_em_memoria: InMemoryUploadedFile = request.FILES.get("img", None)
    tipos_suportados=["image/jpeg","image/png","image/bmp"]
    if request.method == "POST" and (imagem_em_memoria is not None) and (imagem_em_memoria.content_type in tipos_suportados):
        # salva a imagem em um arquivo local
        imagem = Image.open(imagem_em_memoria)
        array_imagem=np.asarray(imagem)

        if(predict(array_imagem)!=None):
            # passa a imagem pra API de ML
            label, confidence = predict(array_imagem)
            if(label!=-1):
                func:Funcionario=Funcionario.get(pk=label)
                if(func!=None):
                    response["id"]=func.pk
                    response["nome"]=func.nome_func
                    response["cargo"]=func.cargo_func
            response["confianca"]=confidence
    # Retorna o resultado da predição

    return response
