from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
import csv

from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista

from .forms import PessoaForm, VeiculoForm, MovRotativoForm, MovMensalistaForm, MensalistaForm

@login_required
def home(request):
    context = {'mensagem':'Olá Ninho' }
    return render(request, 'core/index.html', context)

@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)
@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')    


@login_required
def pessoa_update(request, id):
    data  = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/pessoa_update.html', data)
@login_required   
def pessoa_delete_confirm(request, id):
	pessoa = Pessoa.objects.get(id=id)
	if request.method == 'POST':
		pessoa.delete()
		return redirect('core_lista_pessoas')
	else:
		return render(request, 'core/pessoa_delete_confirm.html', {'pessoa': pessoa})    

@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)

@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')    

@login_required
def veiculo_update(request, id):
    data  = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/veiculo_update.html', data)

@login_required
def veiculo_delete_confirm(request, id):
	veiculo = Veiculo.objects.get(id=id)
	if request.method == 'POST':
		veiculo.delete()
		return redirect('core_lista_veiculos')
	else:
		return render(request, 'core/veiculo_delete_confirm.html', {'veiculo': veiculo})    


@login_required
def lista_movrotativos(request):
    movrotativos = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'movrotativos': movrotativos, 'form': form}
    return render(request, 'core/lista_movrotativos.html', data)

@login_required
def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativo')    

@login_required
def movrotativo_update(request, id):
    data  = {}
    movrotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movrotativo)
    data['movrotativo'] = movrotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativo')
    else:
        return render(request, 'core/movrotativo_update.html', data)

@login_required
def movrotativo_delete_confirm(request, id):
	movrotativo = MovRotativo.objects.get(id=id)
	if request.method == 'POST':
		movrotativo.delete()
		return redirect('core_lista_movrotativo')
	else:
		return render(request, 'core/movrotativo_delete_confirm.html', {'movrotativo': movrotativo})    


@login_required
def lista_movmensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'movmensalistas': movmensalistas, 'form': form}
    movmensalistas = MovMensalista.objects.all()
    return render(request, 'core/lista_movmensalistas.html', data)

@login_required
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalista')    

@login_required
def movmensalista_update(request, id):
    data  = {}
    movmensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movmensalista)
    data['movmensalista'] = movmensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/movmensalistas_update.html', data)

@login_required
def movmensalista_delete_confirm(request, id):
	movmensalista = MovMensalista.objects.get(id=id)
	if request.method == 'POST':
		movmensalista.delete()
		return redirect('core_lista_movmensalista')
	else:
		return render(request, 'core/movmensalista_delete_confirm.html', {'movmensalista': movmensalista})    

@login_required
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', data)

@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')  

@login_required
def mensalista_update(request, id):
    data  = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/mensalista_update.html', data)
    
@login_required    
def mensalista_delete_confirm(request, id):
	mensalista = Mensalista.objects.get(id=id)
	if request.method == 'POST':
		mensalista.delete()
		return redirect('core_lista_mensalista')
	else:
		return render(request, 'core/mensalista_delete_confirm.html', {'mensalista': mensalista})    

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }
        return Render.render('core/relatorio.html', params, 'relatorio_veiculos')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        veiculos = Veiculo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ]) 

        return response