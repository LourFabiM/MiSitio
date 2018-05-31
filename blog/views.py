from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comentario
from .forms import ContactoForm, ComentarioForm
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic.edit import FormView



def post_list(request):
    articulos = Post.objects.filter(published_date__isnull = False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'articulos': articulos})

def detail(request, id_art):
    mostrar = Post.objects.get(id=id_art)
    comentarios = Comentario.objects.filter(post=mostrar).order_by('-fecha')
    return render(request, 'blog/detail.html', {
        'articulo': mostrar,
        'comentarios': comentarios
    })


def contacto_email(request):
    c = ContactoForm(request.POST if request.method == 'POST' else None)
    if c.is_valid():
        #esto tiene que ver con la logica de negocios
        print(c.cleaned_data)
        send_mail(c.cleaned_data['asunto'], c.cleaned_data['su_mensaje'], c.cleaned_data['email'], ['lourfabi07@gmail.com.com'],   fail_silently=False,auth_user=None, auth_password=None, connection=None, html_message=None)
        messages.success(request, 'su mail fue enviado!')
        return redirect('/exito')
    return render(request, 'blog/contacto_email.html', {'form': c})



class ComentarioFormView(FormView):
    form_class = ComentarioForm
    template_name = 'blog/comentario_form.html'

    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs['id_art'])
        comentario = form.save(commit=False)
        comentario.post = post
        comentario.save()
        return redirect('post', id_art=post.id)


class ContactoFormView(FormView):
    form_class = ContactoForm
    template_name = 'blog/contacto_email.html'
    success_url = '/exito'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(c.cleaned_data)
        send_mail(c.cleaned_data['asunto'], c.cleaned_data['su_mensaje'], c.cleaned_data['email'], ['lourfabi07@gmail.com.com'],   fail_silently=False,auth_user=None, auth_password=None, connection=None, html_message=None)
        messages.success(request, 'su mail fue enviado!')
        return super().form_valid(form)


def exito(request):
    return render(request, 'blog/exito.html', {})
