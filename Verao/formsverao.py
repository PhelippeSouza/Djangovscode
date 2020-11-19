from django import forms
from ckeditor.widgets import CKEditorWidget
from .modelsverao import Post

class Postform(forms.ModelForm):  
    conteudo = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ('titulo','conteudo','imagem','status','categoria')