from django.contrib import admin

from .models import CustomUsers, Otdel

@admin.register(CustomUsers)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'superlast_name', 'otdel')
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'superlast_name', 'otdel')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_buh', 'is_glav', 'is_admin', 'is_leed')}),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj=obj)
        if 'deducted_amount' in self.model._meta.get_fields():
            fieldsets[1][1]['fields'] = tuple([field for field in fieldsets[1][1]['fields'] if field != 'deducted_amount'])
        return fieldsets

@admin.register(Otdel)
class OtdelAdmin(admin.ModelAdmin):
    pass