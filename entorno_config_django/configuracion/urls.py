from django.urls import path

from . import views

app_name = 'configuracion'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
]