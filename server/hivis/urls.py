from django.conf.urls import patterns, url

from hivis import views

urlpatterns = patterns('hivis.views',
    url(r'^$', views.index, name='index'),
    url(r'^alignment$', views.alignment, name='alignment'),  
    url(r'^test_alignment$', views.test_alignment, name='test_alignment'),
    url(r'^input_page$', 'input_page'),   
)

