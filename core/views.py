from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages

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
    return render(request, 'produto.html')

    