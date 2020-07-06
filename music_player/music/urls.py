from django.contrib import admin
from django.urls import re_path,include,path
from . import views

urlpatterns=[
    re_path(r'^$',views.index,name='index_page'),
    path('<int:album_id>/',views.detail,name='detail'),
] 