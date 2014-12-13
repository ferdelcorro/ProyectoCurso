# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext

from apps.veterinarian.models import Veterinarian

from apps.veterinary.forms import VeterinaryForm

# Create your views here.
@login_required
def index(request):
    return render_to_response(
                'veterinarian/home.html',
                RequestContext(
                    request,
                    {
                        'mi_nombre': request.user.first_name,
                    }
                )
            )


def sign_up(request):
    form_vet = VeterinaryForm()
    form_user = UserCreationForm()
    if request.method == 'POST':
        form_vet = VeterinaryForm(request.POST)
        form_user = UserCreationForm(request.POST)
        if form_vet.is_valid():
            if form_user.is_valid():
                vet = form_vet.save()
                user = form_user.save()
                veterinarian = Veterinarian.objects.create(
                                    user=user,
                                    veterinary=vet
                                )
                veterinarian.save()
                return index(request)
    return render_to_response(
        'registration/signup.html',
        RequestContext(
            request,
            {
                'form_vet': form_vet,
                'form_user': form_user,
            }
        )
    )
