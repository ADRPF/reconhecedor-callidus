from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from valiface.models import *

import cv2 as cv

# Create your views here.

BASE_DIR = getattr(settings, 'BASE_DIR')

def create_user(request):
    if(int(request.POST['perm']) == 0):
        func = Funcionario(nome_func=request.POST['nome'],
                           cargo_func=request.POST['cargo'],
                           foto_func=request.POST['foto'])
    else:
        pass
    return HttpResponse("Funcionário cadastrado")
    
def teste(request):
    return render(request,
                  'base.html',
                  content_type='text/html')

def display(request):
    return HttpResponse(JsonResponse({'nome': request.POST['nome'],
                                      'cargo': request.POST['cargo'],
                                      'perm': request.POST['perm'],
                                      'foto' : request.POST['image']}))