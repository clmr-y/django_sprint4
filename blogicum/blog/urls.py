"""Blog urls."""

from django.urls import path, include
from . import views

app_name = 'blog'

post_urls = [
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),

    path('<int:post_id>/comment', views.add_comment, name='add_comment'),
    path('<int:post_id>/edit_comment/<int:comment_id>/',
         views.edit_comment,
         name='edit_comment'),

    path('<int:post_id>/delete_comment/<int:comment_id>/',
         views.delete_comment,
         name='delete_comment'),
]

profile_urls = [
    path('edit/',
         views.edit_profile,
         name='edit_profile'),
    path('<str:username>/',
         views.profile,
         name='profile'),

]

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', include(post_urls)),
    path('profile/', include(profile_urls)),
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts'),
]
