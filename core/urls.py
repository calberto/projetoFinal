from django.urls import path 
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoa_novo,
    veiculo_novo,
    movrotativo_novo,
    movmensalista_novo,
    mensalista_novo,
    pessoa_update,
    pessoa_delete_confirm,
    veiculo_update,
    veiculo_delete_confirm,
    movrotativo_update,
    movrotativo_delete_confirm,
    movmensalista_update,
    movmensalista_delete_confirm,
    mensalista_update,
    mensalista_delete_confirm,
    Pdf,
    ExportarParaCSV,
) 

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>/', pessoa_delete_confirm, name='core_pessoa_delete_confirm'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculos-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<int:id>/', veiculo_update, name='core_veiculo_update'),
    path('veiculo-delete/<int:id>/', veiculo_delete_confirm, name='core_veiculo_delete_confirm'),
    
    path('movrotativos/', lista_movrotativos, name='core_lista_movrotativo'),
    path('movrotativo-novo/', movrotativo_novo, name='core_movrotativo_novo'),
    path('movrotativo-update/<int:id>/', movrotativo_update, name='core_movrotativo_update'),
    path('movrotativo-delete/<int:id>/', movrotativo_delete_confirm, name='core_movrotativo_delete_confirm'),

    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista-update/<int:id>/', mensalista_update, name='core_mensalista_update'),
    path('mensalista-delete/<int:id>/', mensalista_delete_confirm, name='core_mensalista_delete_confirm'),

    
    path('movmensalistas/', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('movmensalista-novo/', movmensalista_novo, name='core_movmensalista_novo'),
    path('movmensalista-update/<int:id>/', movmensalista_update, name='core_movmensalista_update'),
    path('movmensalista-delete/<int:id>/', movmensalista_delete_confirm, name='core_movmensalista_delete_confirm'),
    path('relatorio/', Pdf.as_view(), name='relatorio_pdf'),
    path('relatorio-csv/', ExportarParaCSV.as_view(), name='relatorio_csv')

]