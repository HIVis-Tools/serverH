from django.conf.urls import patterns, url

from hivis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^alignment$', views.alignment, name='alignment'),    
)