from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactHelp
from .models import QuemSomos, Portfolio, Clientes, Servicos

def website(request):

    template_name = 'index.html'
    context_dict = {}
    context_dict['data'] = QuemSomos.objects.last()
    context_dict['gente'] = Clientes.objects.all()
    context_dict['stuff'] = Portfolio.objects.all()
    context_dict['opcoes'] = Servicos.objects.all()
    context_dict['form'] = ContactHelp()

    if request.method == 'POST':
        form = ContactHelp(request.POST)
        if form.is_valid():
            context_dict['is_valid'] = True
            #form.send_mail()
            form = ContactHelp()
    else:
        form = ContactHelp()

    return render(request, template_name, context_dict)
