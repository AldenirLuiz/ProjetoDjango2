from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
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

    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)

            print(f'Nome: {prod.nome}')
            print(f'Preço: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')

            messages.success(request, 'Produto Salvo com Sucesso.')
            form = ProdutoModelForm()
        else:
            messages.error(request,'Erro ao Salvar Produto.')
    else:
        form = ProdutoModelForm()
    
    context = {
        'form': form
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
    