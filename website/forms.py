from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactHelp(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome', 'data-rule':'required', 'data-msg': 'Este campo e obrigatorio.'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(xx)xxxxxxxxx', 'data-rule':'required', 'data-msg': 'Por favor, insira pelo menos 9 caracteres.'}), max_length=11)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@exemplo.com', 'data-rule':'required'}), label='E-mail')
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Duvida/Mensagem', 'data-rule':'required', 'rows':5}))

    def send_mail(self):
        subject = self.cleaned_data['nome']
        message = 'Nome: %(nome)s\n Telefone: %(telefone)s\n E-mail: %(email)s\n\n %(mensagem)s'
        context = {
            'nome': self.cleaned_data['nome'],
            'telefone': self.cleaned_data['telefone'],
            'email': self.cleaned_data['email'],
            'mensagem': self.cleaned_data['mensagem']
        }

        message = message % context
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,[settings.CONTACT_EMAIL])
