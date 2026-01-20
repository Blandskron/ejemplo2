from django.shortcuts import render, redirect
from .forms import FormularioContacto

def landing(request):
    return render(request, 'configuracion/landing.html')

def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            form.save()  # Esto guarda los datos en la base de datos automáticamente
            return redirect('configuracion/landing') # Redirige a inicio tras el éxito
    else:
        form = FormularioContacto()
    
    return render(request, 'configuracion/contacto.html', {'form': form})

def sobre_nosotros(request):
    return render(request, 'configuracion/sobrenosotros.html')