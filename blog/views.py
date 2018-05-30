from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .forms import ContactoForm
from django.core.mail import send_mail




def post_list(request):
    articulos = Post.objects.filter(published_date__isnull = False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'articulos': articulos})

def detail(request, id_art):
    mostrar = Post.objects.get(id=id_art)
    return render(request, 'blog/detail.html', {'articulo': mostrar})


def contacto_email(request):
    c = ContactoForm()
    
    if request.method == 'POST':
        c = ContactoForm(request.POST)
        
        if c.is_valid():
            #esto tiene que ver con la logica de negocios
            print(c.cleaned_data)
            
            send_mail(c.cleaned_data['asunto'], c.cleaned_data['su_mensaje'], c.cleaned_data['email'], ['lourfabi07@gmail.com.com'],   fail_silently=False,auth_user=None, auth_password=None, connection=None, html_message=None)
            
            return redirect('/exito')

    return render(request, 'blog/contacto_email.html', {'form': c})

def exito(request):
    return render(request, 'blog/exito.html', {})
