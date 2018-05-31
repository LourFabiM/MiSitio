
from django import forms
from .models import Post, Comentario


class ContactoForm(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField(required = True)
    su_mensaje = forms.CharField(widget = forms.Textarea())

    def clean_email(self):
        data = self.cleaned_data['email']
        if not data.endswith('@escuela.edu.ar'):
            raise forms.ValidationError("El e-mail debe ser ejemplo@escuela.edu.ar")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['nombre', 'comentario']