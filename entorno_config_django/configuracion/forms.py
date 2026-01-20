from django import forms
from .models import ConsultaContacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = ConsultaContacto
        fields = ['nombre', 'email', 'mensaje']
        # Añadimos clases de Bootstrap para que se vea bien
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@ejemplo.com'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu mensaje...'}),
        }