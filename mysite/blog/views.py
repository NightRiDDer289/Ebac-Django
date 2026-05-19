from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Post

class PostView(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'

class PostDetail(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'