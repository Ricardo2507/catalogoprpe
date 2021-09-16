from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('materiais/', views.materiais, name='materiais'),
    path('<slug:conta_slug>/', views.materiais, name='materiais_by_conta'),
    path('contas/', views.contas, name='contas'),
    path('detalhes/<int:material_id>/', views.detalhes, name='detalhes'), 
    # path('busca/', views.busca, name='busca'),
]