from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from src import settings
from src.pair_stairs.views import add_programmer, view_stairs, update_times

urlpatterns = patterns('',
    url(r'^add_programmer/', add_programmer),
    url(r'^stairs/', view_stairs),
    url(r'^update_times/(?P<pairs>.+)$', update_times),
    # Examples:
    # url(r'^$', 'srcs.views.home', name='home'),
    # url(r'^srcs/', include('srcs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
