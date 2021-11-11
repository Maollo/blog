from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.

from post.models import post

class posthome(ListView):
    model = post    
    template_name = 'post/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pManager'] = post.postados.all()
        return context


class postdetail(DetailView):
    model = post
    template_name = 'post/post_detail.html'