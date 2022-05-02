from django.shortcuts import render
from django.views import generic
from .models import Post, Artist

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class ArtistList(generic.ListView):
    queryset = Artist.objects.order_by('-name')
    template_name = 'artists.html'
