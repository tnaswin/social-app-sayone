from django.urls import path
from .views import post_create_and_list_view, like_unlike_post, post_serialized_view

app_name = 'posts'

urlpatterns = [
    path('', post_create_and_list_view, name='main-post-view'),
    path('liked/', like_unlike_post, name='like-post-view'),
    path('serialized/', post_serialized_view, name='serialized-view'),
]