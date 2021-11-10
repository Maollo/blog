from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import OrderBy
# Create your models here.
class post (models.Model):
    estado_post = (
        (('Postado'),('postado')),
        (('Rascunha'),'rascunha')
    )
    titulo = models.CharField(max_length=15,blank=False,null=False)
    slug = models.SlugField(max_length=15,auto_created='titulo',blank=True,null=True)
    descricao = models.TextField(max_length=200,blank=True,null=True,name='descrição')
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    datacriacao = models.DateTimeField(auto_created=True)
    datademodificacao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to ='static/imgs/',blank=True,null=True )
    estado_atual = models.CharField(max_length=15,choices=estado_post)
    
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo','autor', 'datacriacao']