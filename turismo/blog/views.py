from django.shortcuts import render, get_object_or_404
from .models import Post

# Añadimos una funcion que realiza la peticion a las rutas que son las vistas al usuario
# enviada desde el parametro del modelo y del proyecto creado a la vista HTML

def renderPosts(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    return render(request, "blog.html", {"posts": posts, "total_posts": total_posts})
# Añadimos una funcion que realiza la peticion a las rutas que son las vistas al usuario
# enviada desde el parametro del modelo y del proyecto creado a la vista HTML

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})
