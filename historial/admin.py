from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import AutosizedTextarea, LinkedSelect
from import_export.admin import ImportExportModelAdmin
from .models import Bug, Componente
from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied


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


if getattr(settings, 'SOCIAL_AUTH_USE_AS_ADMIN_LOGIN', False):

    def _social_auth_login(self, request, **kwargs):
        if request.user.is_authenticate():
            if not request.user.is_active or not request.user.is_staff:
                raise PermissionDenied()
        else:
            return redirect_to_login(request.get_full_path())
    
    admin.sites.AdminSite.login = _social_auth_login

admin.site.register(Bug, BugAdmin)
admin.site.register(Componente, ComponenteAdmin)
