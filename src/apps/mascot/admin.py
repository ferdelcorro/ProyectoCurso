from django.contrib import admin
from apps.mascot.models import Mascot, Species, Race


admin.site.register(Mascot)
admin.site.register(Species)
admin.site.register(Race)