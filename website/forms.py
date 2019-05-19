from django import forms
#from .models import Post

class ContactHelp(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome', 'data-rule':'minlen:4', 'data-msg': 'Por favor, insira pelo menos 3 caracteres.'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(xx)xxxxxxxxx', 'data-rule':'minlen:4', 'data-msg': 'Por favor, insira pelo menos 9 caracteres.'}), max_length=11)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@exemplo.com', 'data-rule':'minlen:4'}), label='E-mail')
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Duvida/Mensagem', 'data-rule':'minlen:4'}))
