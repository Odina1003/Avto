from django.shortcuts import render
from django.http import HttpResponse
from .models import Avto

# Create your views here.
def main(request):
    avtos = Avto.objects.all
    print(avtos)
    return render(request=request, context={}, template_name='index.html')
