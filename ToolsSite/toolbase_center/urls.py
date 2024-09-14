from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home_page_view, name='index'),
    path('cat/', views.about_tool, name='show'),
    path('dogs/', views.rat_tool, name='life'),
    path('panda/', views.dense_tool, name='care'),
    path('lion/', views.detect_tool, name='hate'),
]
