from django import forms
from django.core.mail import send_mail
from django.conf import settings
#from .import views

class ContactHelp(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome', 'data-rule':'required', 'data-msg': 'Por favor, insira pelo menos 3 caracteres.'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(xx)xxxxxxxxx', 'data-rule':'required', 'data-msg': 'Por favor, insira pelo menos 9 caracteres.'}), max_length=11)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@exemplo.com', 'data-rule':'required'}), label='E-mail')
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Duvida/Mensagem', 'data-rule':'required'}))

    def send_mail(self):
        subject = self.cleaned_data['name']
        message = 'Nome: %(name)s\n Telefone: %(telefone)s\n E-mail: %(email)s\n\n %(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'telefone': self.cleaned_data['telefone'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }

        message = message % context
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,[settings.CONTACT_EMAIL])
