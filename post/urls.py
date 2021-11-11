from django.urls import path
from post.views import posthome, postdetail

name_app = 'post'


urlpatterns = [
    path('',posthome.as_view(),name='home'),
    path('<int:pk>', postdetail.as_view(), name='Postdetail'),
] 