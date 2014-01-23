from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView 
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bugscontrol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', RedirectView.as_view(url='/admin/')),
    url(r'^index/', 'historial.views.index', name='index'),
    
    url(r'', include('social_auth.urls')), 
    url(r'^login/$', 'social_auth.views.auth', {'backend': 'google'}, name='login'),
)
