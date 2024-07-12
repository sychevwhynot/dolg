from django.contrib import admin
from .models import Shtraf, Spisanie


class ShtrafAdmin(admin.ModelAdmin):
    pass

admin.site.register(Shtraf, ShtrafAdmin)

class SpisanieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Spisanie, SpisanieAdmin)