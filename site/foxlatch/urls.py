from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon.ico/$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^$', 'fox.views.index_view', name='index_view'),
    url(r'^about/$', 'fox.views.about_view', name='about_view'),
    url(r'^register/$', 'fox.views.FoxRegistration'),
    url(r'^login/$', 'fox.views.LoginRequest'),
    url(r'^logout/$', 'fox.views.LogoutRequest'),
    url(r'^profile/$', 'fox.views.Profile'),
)
