from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from post.models import post

class posthome(ListView):
    model = post    
    template_name = 'post/home.html'