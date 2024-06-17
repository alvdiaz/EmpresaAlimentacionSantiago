from django.shortcuts import render
from .forms import PedidoForm

# Create your views here.
# restaurant/views.py
def home(request):
    form = PedidoForm()
    return render(request, 'restaurant/home.html', {'form': form})