from django.contrib import admin
from . models import *
from  django.utils.html import format_html


class ContaAdmin(admin.ModelAdmin):
    prepopulated_fields =  {'slug': ('descricao',)}
    list_display = ('conta', 'descricao','slug')
    

class MaterialAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px"/>'.format(object.image_url.url))
    
    thumbnail.short_description = 'Photo'
        
    prepopulated_fields =  {'slug': ('codigo',)}                   
    list_display = ('codigo', 'thumbnail', 'slug','desc_material', 'unidade', 'conta')
    list_display_links = ('codigo', 'thumbnail', 'desc_material', )
    search_fields = ('codigo', 'desc_material',)
    list_filter = ('desc_material', )

admin.site.register(Conta, ContaAdmin)
admin.site.register(Material, MaterialAdmin)