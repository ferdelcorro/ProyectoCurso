# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.http import Http404

from apps.veterinarian.views import index

from apps.client.models import Client
from apps.mascot.models import Mascot
from apps.veterinarian.models import Veterinarian

from apps.mascot.forms import MascotForm

# Create your views here.
@login_required
def cargar_mascota(request, pk=None):
    form_mascot = MascotForm()
    v = get_object_or_404(Veterinarian, user=request.user)

    if pk is not None:
        c = get_object_or_404(Client, pk=pk, veterinary=v.veterinary)

    if request.method == 'POST':
        form = MascotForm(request.POST)
        c = request.POST["owner"]

        if form.is_valid():
            mascot = form.save(commit=False)
            owner = get_object_or_404(
                            Client,
                            pk=c
                    )
            mascot.owner = owner
            mascot.save()

            c = Client.objects.get(pk=c)
            m = Mascot.objects.filter(owner=c)
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
            
    return render_to_response(
        'mascot/cargar_mascota.html',
        RequestContext(
            request,
            {
                'form': form_mascot,
                'cliente': c.pk
            }
        )
    )

@login_required
def mostrar_mascota(request, pk=None):
    v = get_object_or_404(Veterinarian, user=request.user)

    if pk is not None:
        m = get_object_or_404(Mascot, pk=pk)

        if v.veterinary == m.owner.veterinary:

            return render_to_response(
                'mascot/mostrar_mascota.html',
                RequestContext(
                    request,
                    {
                        'mascota': m
                    }
                )
            )

        else:
            return Http404

    else:
        return index(request)