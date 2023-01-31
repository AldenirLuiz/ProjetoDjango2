from django.db import models
from stdimage import StdImageField
from datetime import datetime

# Signals
from django.db.models import signals
from django.template.defaultfilters import slugify




class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


class PlanilhaCob(Base):
    dateNow = datetime.now().date()
    nome = models.CharField('Nome da Rota', max_length=100, default='Cidade')
    data = models.DateField('Data da Rota', default=datetime.strftime(dateNow , "%d/%m/%Y"))
    preco = models.IntegerField('Valor Cobrado', default="10.000")
    estoque = models.IntegerField('Mercadoria de Estoque', default="12.000")

    def __str__(self) -> str:
        strFormat = f'''
            {self.nome} \t {datetime.strftime(self.dateNow , "%d/%m/%Y")}
        '''
        return strFormat

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)
    

signals.pre_save.connect(produto_pre_save, sender=Produto)
