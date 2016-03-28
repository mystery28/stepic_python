from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    url(r'^$', 'main', name='main'),
    url(r'^login/.*', 'test', name='login'),
    url(r'^signup/.*', 'test', name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', 'question', name='question'),
    url(r'^ask/.*', 'test', name='ask'),
    url(r'^popular/.*', 'popular', name='popular'),
    url(r'^new/.*', 'test', name='new'),
)
