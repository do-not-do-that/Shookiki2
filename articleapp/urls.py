from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, \
    ArticleListView, private_view

app_name = 'articleapp'

urlpatterns = [

    path('list/',ArticleListView.as_view(),name='list'),
    path('private/',private_view,name='private'),
    path('create/',ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>',ArticleDetailView.as_view(),name='detail'),
    path('update/<int:pk>',ArticleUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',ArticleDeleteView.as_view(),name='delete'),
]