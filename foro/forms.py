from django import forms
from .models import Post, Comentario
from crispy_forms.layout import Field, Layout
from crispy_forms.helper import FormHelper

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('id_foro', 'title', 'content')


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['contenido_comentario'].widget.attrs['rows'] = 4

    class Meta():
        model = Comentario
        fields = ('contenido_comentario',)