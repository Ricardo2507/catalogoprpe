from .models import Conta

# deve ser incluído no settings  em TEMPLATES
# cria dicionário com todas as categorias e passa para template
# retorna dicionário como contexto
def menu_links(request):
    links = Conta.objects.all()
    return dict(links=links)