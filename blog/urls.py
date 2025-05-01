from django.urls import path
from .views import postReader, post_detail, PostUpdateView, PostDeleteView


urlpatterns = [
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path("", postReader, name='posts'),
    path("post/<int:pk>", post_detail, name='post-view'),
]