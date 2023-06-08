from django.urls import path
from .views import blog, index, post, search, post_delete, post_update, post_create

app_name= "posts"

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='post-list'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete', post_delete, name='post-delete'),
    path('search/', search, name='search'),
    path('create/', post_create, name='post-create'),


]