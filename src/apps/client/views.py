# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.db.models import Q 

from apps.veterinarian.views import index
from apps.mascot.views import cargar_mascota

from apps.veterinarian.models import Veterinarian
from apps.client.models import Client
from apps.mascot.models import Mascot

from apps.client.forms import ClientForm
from apps.mascot.forms import MascotForm

# Create your views here.
@login_required
def cargar_cliente(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            print client.id
            veterinarian = get_object_or_404(
                                Veterinarian,
                                user=request.user
                            )
            client.veterinary = veterinarian.veterinary
            client.save()
            print client.id
            form_mascot = MascotForm()
            return render_to_response(
                'mascot/cargar_mascota.html',
                RequestContext(
                    request,
                    {
                        'form': form_mascot,
                        'cliente': client.pk
                    }
                )
            )

    return render_to_response(
        'client/cargar_cliente.html',
        RequestContext(
            request,
            {
                'form': form,
            }
        )
    )

@login_required
def buscar_cliente(request):
    v = get_object_or_404(Veterinarian, user=request.user)
    c = Client.objects.filter(veterinary=v.veterinary)

    return render_to_response(
        'client/buscar_cliente.html',
        RequestContext(
            request,
            {
                'clientes': c,
            }
        )
    )

@login_required
def mostrar_cliente(request, pk=None):
    v = get_object_or_404(
            Veterinarian,
            user=request.user
        )

    if pk is not None:
        c = get_object_or_404(
                Client,
                pk=pk,
                veterinary=v.veterinary
            )
        m = Mascot.objects.filter(owner__pk=c.pk)

        return render_to_response(
            'client/mostrar_cliente.html',
            RequestContext(
                request,
                {
                    'cliente': c,
                    'mascotas': m
                }
            )
        )

    else:
        return buscar_cliente(request)