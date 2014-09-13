from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^$', include('hivis.urls')),
    #url(r'^$', 'server.views.home', name='home'),
    url(r'^hivis/', include('hivis.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # redirect everything else to hivis view
    url(r'^$', RedirectView.as_view(url='hivis/', permanent=False), name='index')
)
