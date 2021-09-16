from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

class Conta(models.Model):
    conta = models.CharField(max_length=9)
    descricao = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    
    class Meta:
        verbose_name = 'conta'
        verbose_name_plural = 'contas'
    
    def __str__(self):
        return self.conta + ' ' + self.descricao
    
    def get_absolute_url(self):
       
        return reverse('materiais_by_conta', args=[self.slug])
    
class Material(models.Model):
    codigo = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100,unique=True)
    desc_material = models.CharField(max_length=200)
    unidade = models.CharField(max_length=30)
    conta = models.ForeignKey(Conta, null=True, on_delete=models.SET_NULL)
    image_url = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materiais'
    
    def __str__(self):
      
        return self.codigo + ' - ' +  self.desc_material 
    
    # def get_absolute_url(self):
    #     print(self)
    #     return reverse('detalhes',args=[self.slug])
