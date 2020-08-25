from django.urls import path

from .views import posts_list, post_detail, tags_list, tag_detail


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tags/', tags_list, name='tags_detail_url'),
    path('tags/<str:slug>', tag_detail, name='tag_detail_list_url')
]
