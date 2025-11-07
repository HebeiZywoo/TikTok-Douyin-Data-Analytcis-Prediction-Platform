from django.contrib import admin
from django.urls import path, include
from video import views

urlpatterns = [
    path('', views.login, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('comment_list/', views.comment_list, name='comment_list'),
    path('part1/', views.part1, name='part1'),
    path('part2/', views.part2, name='part2'),
    path('part3/', views.part3, name='part3'),
    path('part4/', views.part4, name='part4'),
    path('part5/', views.part5, name='part5'),
    path('part6/', views.part6, name='part6'),
    path('predict/', views.predict, name='predict'),
    path('get_ai/', views.get_ai, name='get_ai'),
    path('changeInfo/', views.changeInfo, name='changeInfo'),
    path('logout/', views.logout, name='logout'),

]
