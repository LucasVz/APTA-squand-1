from django import forms
#from .models import Post

class ContactHelp(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    telefone = forms.CharField(label='telefone', max_length=12)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Duvida/Mensagem', widget=forms.Textarea)

    #class Meta:
    #    model = Post
    #    fields = ('title', 'text',)
