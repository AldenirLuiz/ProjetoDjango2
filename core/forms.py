from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto, PlanilhaCob

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.CharField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema Django2',
            body=conteudo,
            from_email='aldenir.sky@gmail.com',
            to=['contato@dominio.com',],
            headers={'Reply-To:': email}
        )

        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']


class PlanilhaModelForm(forms.ModelForm):
    class Meta:
        model = PlanilhaCob
        fields = ['nome', 'data', 'preco', 'estoque']