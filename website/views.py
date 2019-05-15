from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactHelp
from .models import QuemSomos, Portfolio, Clientes, Servicos

def website(request):

    #if request.method == 'POST':
    #    form = ContactHelp(request.POST)
    #    if form.is_valid():
    #        name = form.cleaned_data['name']
    #        email = form.cleaned_data['']

    template_name = 'index.html'
    context_dict = {}
    context_dict['data'] = QuemSomos.objects.last()
    context_dict['gente'] = Clientes.objects.all()
    context_dict['stuff'] = Portfolio.objects.all()
    context_dict['opcoes'] = Servicos.objects.all()
    #context_dict['form'] = form
    #form = ContactHelp()
    return render(request, template_name, context_dict)

    #{'stuff':stuff}, {'opcoes':opcoes}, {"form": form})
