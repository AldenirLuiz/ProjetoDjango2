from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            print('Mensagem Enviada')
            print(
                f'''
                    Nome: {nome}
                    E-mail: {email}
                    Assunto {assunto}
                    Mensagem: {mensagem}''')
            messages.success(request, 'E-mail enviado.')
        else: messages.error(request, 'ERRO! O E-mail Nao foi enviado.')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    context = {
        'services': service(3, 3)
    }
    return render(request, 'produto.html', context)

def service(line, column):
    result = ""
    count = 0
    for x in range(line):
        result += '<br>'
        for y in range(column):
            count+=1
            result += f"""<button class="btn calc" id="btn-{str(count)}" onclick=sumInt("{str(count)}")>{str(count)}</button>"""
    return result
    
def myCalc(request, arg):
    myList = list(arg)

    print(myList)
    return render(request, 'all rights')
    