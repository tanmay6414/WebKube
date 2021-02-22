from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contextname/', views.contextname, name='KubrnetesCrud-contextname'),
    path('getcontexts/', views.getcontexts, name='KubrnetesCrud-getcontexts'),
    path('changecontexts/', views.changecontexts, name='KubrnetesCrud-changecontexts'),
    path('listpodinnamespace/', views.listpodinnamespace, name='KubrnetesCrud-listpodinnamespace'),
    path('getpoddetail/', views.getpoddetail, name='KubrnetesCrud-getpoddetail'),
]