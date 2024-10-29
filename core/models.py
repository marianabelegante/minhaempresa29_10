from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Cargo(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.descricao


class Funcionario(Base):
    nome = models.CharField(max_length=200)
    bio = models.TextField()
    foto = StdImageField(upload_to='equipe',
                         variations={'thumb':{'width':500,
                                              'height':500,
                                              'crop':True}})
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL,
                              blank=True, null=True)

    facebook = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    linkedin = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'


    def __str__(self):
        return self.nome


class Servico(Base):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    imagem = StdImageField(upload_to='servicos', variations={'thumb':{'width':300,
                                                                      'height':300,
                                                                      'crop':True}})

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.titulo
