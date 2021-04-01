from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(),name='app-home'),
    path('about/',views.about,name='app-about')
]