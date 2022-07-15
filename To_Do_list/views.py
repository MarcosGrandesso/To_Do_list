from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from tasks.forms import tarefasForm
from django.contrib import messages
from tasks.models import Prioridade, Tarefas
from django.contrib.auth.models import User
from tasks.models import Tarefas

@login_required(login_url='login')
def index(request):
    lista = Tarefas.objects.all()

    context = {'nome': 'marquin',
                'lista': lista}
    

    if request =='POST':
        nome = request.POST.get('nome',None)
        sobrenome = request.POST.get('nome',None)
        print(nome)

    return render(request, 'index.html', context)
    

def new_task(request):
    lista = Tarefas.objects.all()

    context = {'nome': 'marquin',
                'lista': lista}
    
    if request.method == 'POST':
        print('uepa')
        nome = request.POST.get('nome',None)
        descriçao = request.POST.get('descriçao',None)
        imagem = request.POST.get('imagem', None)
        prioridade = request.POST.get('prioridade',None)

        prioridade= prioridade.upper()

        if prioridade in ('ALTA'):
            prioridade= Prioridade.objects.get(nivel = 'Alta')
        elif prioridade in ('MEDIA'):
            prioridade= Prioridade.objects.get(nivel = 'Média')
        elif prioridade in ('BAIXA'):
            prioridade= Prioridade.objects.get(nivel = 'Baixa')
            
        else:
            messages.error(
                request,
                'Prioridade errada a sintaxe é Alta/Media/Baixa')
            return render(request, 'taskn.html')
        
        tarefa = Tarefas.objects.create(nome= nome, descriçao= descriçao, prioridade= prioridade, imagem= imagem)
        tarefa.save()
        return redirect('index')

    return render(request, 'taskn.html', context)


def register(request):
    if request.method=='POST':
        usuario = request.POST.get('usuario',None)
        senha = request.POST.get('senha',None)
        senha2 = request.POST.get('senha2',None)
    
        if senha == senha2 and len(senha) > 8:

            user = User.objects.create_user( username= usuario, password =senha)
            user.save()
            return redirect('index')

    return render(request, 'register.html' )

def login(request):
    if request.method=='POST':
        redirect('index')
    return render(request,'registration/login.html')