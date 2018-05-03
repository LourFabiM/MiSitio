from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


def post_list(request):
    articulos = Post.objects.filter(published_date__isnull = False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'articulos': articulos})

def detail(request, id_art):
    mostrar = Post.objects.get(id=id_art)
    return render(request, 'blog/detail.html', {'articulo': mostrar})
