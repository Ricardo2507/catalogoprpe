from django.shortcuts import render, get_object_or_404
from . models import Material, Conta
from django.core.paginator import Paginator


def index(request):
    return render(request, 'material/index.html')


def materiais(request, conta_slug=None):
    materiais = None
    contas = None
    materiais_count = 0
    if conta_slug != None:
        contas = get_object_or_404(Conta, slug=conta_slug)
        materiais = Material.objects.all().filter(conta=contas).order_by('codigo')
        materiais_count = materiais.count() 
    else:
      materiais = Material.objects.all().order_by('codigo')
  
    search = request.GET.get('search')
    if search:
        materiais = materiais.filter(desc_material__icontains=search)
        
        # ver paginação na documentação do Django
    
        # # vamos sobrescrever os materiais
    paginator = Paginator(materiais, 10)  # Show 25 contacts per page
        
    page = request.GET.get('p')
    materiais = paginator.get_page(page)
    contexto = {'materiais': materiais,
                'materiais_count': materiais_count,
                'conta_slug': conta_slug}
    
        #print(materiais.previous_page_number)
        #print(materiais.number)
    return render(request, 'material/materiais.html', contexto)

def contas(request):
    contas = Conta.objects.all().order_by('conta')
    
    search = request.GET.get('search')
    if search:
       contas = contas.filter(descricao__icontains=search)
    
    # ver paginação na documentação do Django
   
    # # vamos sobrescrever os materiais
    paginator = Paginator(contas, 10)  # Show 25 contacts per page
    page = request.GET.get('p')
    contas = paginator.get_page(page)
    contexto = {'contas': contas}
   
    #print(materiais.previous_page_number)
    #print(materiais.number)
    return render(request, 'material/contas.html', contexto)

def detalhes(request, material_id):
     
    materiais = get_object_or_404(Material, pk=material_id)

    try:
        materiais = Material.objects.get(pk=material_id)

        #     # print(request.POST['song'])
        #empenho = empenho.empenho_set.get(pk=request.GET['empenho'])

    except (KeyError, Material.DoesNotExist):

        return render(request, 'material/detalhe.html', {
            'materiais': materiais,
            'error_message': 'Não foi selecionado nenhum material',
        })
    contexto = {'materiais': materiais}
    return render(request, 'material/detalhe.html', contexto)
    

