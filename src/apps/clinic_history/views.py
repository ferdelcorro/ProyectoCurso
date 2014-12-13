from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import Http404

from apps.veterinarian.views import index

from apps.veterinarian.models import Veterinarian
from apps.mascot.models import Mascot
from apps.clinic_history.models import ClinicHistory

from apps.clinic_history.forms import HistoryForm

# Create your views here.
@login_required
def cargar_historial(request, pk=None):
    form = HistoryForm()
    v = get_object_or_404(Veterinarian, user=request.user)

    if pk is not None:
        m = get_object_or_404(Mascot, pk=pk)

        if v.veterinary == m.owner.veterinary:
            pass
        else:
            return Http404

    if request.method == 'POST':
        mascota = request.POST["mascota"]
        m = get_object_or_404(Mascot, pk=mascota)
        if v.veterinary == m.owner.veterinary:
            form = HistoryForm(request.POST)

            if form.is_valid():
                h = form.save(commit=False)
                h.mascot = m
                h.save()
                return historiales(request, m.pk)

    return render_to_response(
        'clinic_history/cargar_historial.html',
        RequestContext(
            request,
            {
                'form': form,
                'mascota': m.id,
                'cliente': m.owner.id
            }
        )
    )

@login_required
def historiales(request, pk=None):
    v = get_object_or_404(Veterinarian, user=request.user)

    if pk is not None:
        m = get_object_or_404(Mascot, pk=pk)

        if v.veterinary == m.owner.veterinary:
            h = ClinicHistory.objects.filter(mascot=m)

            return render_to_response(
                'clinic_history/list.html',
                RequestContext(
                    request,
                    {
                        'historiales': h,
                        'mascota': m.id,
                        'cliente': m.owner.id
                    }
                )
            )
        else:
            return Http404

    else:
        return index(request)