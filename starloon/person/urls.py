from django.urls import path
from . import views

APP_NAME: 'person '

urlpatterns = [
	path('',views.index,name ='index'),
    path('search/',views.searchBar,name ='search'),
    path('<slug:slug>/', views.detail, name = 'detail'),
]


