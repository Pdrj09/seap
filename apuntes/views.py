from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import cons_apunt
from .models import apuntes
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def index(request):
    ctx = {
        'form': cons_apunt(),
        }
    if request.method == "POST":
        form = cons_apunt(request.POST)

        if form.is_valid():

            try:
                dirpy = apuntes.objects.get(nombre_tema=form.cleaned_data['nombre_tema'])
                dir = '/' + str(dirpy.id) +'/archivos'
                return redirect(dir)
            except ObjectDoesNotExist:
                return redirect('/')

    return render(request, 'templates/busqueda.html', ctx)


def archivos(request, apuntes_id):
    archivo = apuntes.objects.get(pk=apuntes_id)
    template = archivo.dir
    context={
        'ap':apuntes_id,
    }
    return render(request, str(template), context)
