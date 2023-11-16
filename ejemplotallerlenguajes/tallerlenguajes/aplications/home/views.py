from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Prueba
from .forms import PruebaForm
# Create your views here.

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = 'crear.html'
    form_class = PruebaForm
    success_url = '/listar'

class PruebaListView(ListView):
    model =Prueba
    template_name= 'listar.html'
    

class PruebaUpdateView(UpdateView):
    model = Prueba
    template_name = 'crear.html'
    form_class = PruebaForm
    success_url = '/listar'

class PruebaDeleteView(DeleteView):
    model=Prueba
    template_name= 'eliminarc.html'
    success_url= '/listar'

from django.shortcuts import render

def index(request):
    return render(request, 'hv.html')