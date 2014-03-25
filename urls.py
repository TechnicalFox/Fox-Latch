from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/users/u21/technicalfox/Projects/FoxLatch/foxlatch/static/'}),

    url(r'^admin/', include(admin.site.urls)),
)
