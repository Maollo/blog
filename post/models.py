from django.db import models
from django.contrib.auth.models import User
from django.db.models.manager import Manager
from django.urls import reverse
# Create your models here.

#manager dos postados.
class postadoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(estado_atual='postado')



class post (models.Model):
    estado_post = (
        (('postado'),('postado')),
        (('rascunha'),'rascunha')
    )
    titulo = models.CharField(max_length=15,blank=False,null=False)
    slug = models.SlugField(max_length=15,auto_created='titulo',blank=True,null=True)
    descricao = models.TextField(max_length=200,blank=True,null=True,name='descrição')
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    datacriacao = models.DateTimeField(auto_created=True)
    datademodificacao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to ='imgs/',blank=True,null=True )
    estado_atual = models.CharField(max_length=15,choices=estado_post)
    
    objects = models.Manager()
    postados = postadoManager()
    
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-datacriacao']

    def get_absolute_url(self):
        return reverse("Postdetail", kwargs={"pk": self.pk})
    
    