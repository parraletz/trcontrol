from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import AutosizedTextarea, LinkedSelect
from import_export.admin import ImportExportModelAdmin
from .models import Bug, Componente



class BugAdminForm(ModelForm):
    class Meta:
        widgets = {
            'observaciones' : AutosizedTextarea(attrs={'rows':8, 'class': 'input-x-large'}),
            'componente': LinkedSelect,
            'producto': LinkedSelect,
        }


class BugAdmin(ImportExportModelAdmin):
    list_display = ('numero', 'liga', 'componente', 'producto', 'observaciones', 'status', )
    list_display_links = ('numero', 'liga')

    form = BugAdminForm




class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('componente', 'version', 'activo')

admin.site.register(Bug, BugAdmin)
admin.site.register(Componente, ComponenteAdmin)
