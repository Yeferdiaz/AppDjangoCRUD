from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('', views.index, name='index'),
    path('',  views.PruebaCreateView.as_view()),
    path('crear/',  views.PruebaCreateView.as_view()),
    path('listar/',  views.PruebaListView.as_view()),
    path('actualizar/<int:pk>',  views.PruebaUpdateView.as_view()),
    path('eliminar/<int:pk>',  views.PruebaDeleteView.as_view()),
    
]
