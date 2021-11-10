from django.urls import path
from post.views import posthome

name_app = 'post'


urlpatterns = [
    path('',posthome.as_view(),name='home'),
]