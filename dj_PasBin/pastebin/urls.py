# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = patterns('pastebin.views',
                       url(r'^$', 'index', name='djpaste_index'),
                       url(r'^help/$', TemplateView.as_view(template_name='dj_PasBin/help.html'), name='djpaste_help'),
                       url(r'^paste/(?P<id>\d+)/$', 'paste_details', name='djpaste_paste_details'),
                       url(r'^plain/(?P<id>\d+)/$', 'plain', name='djpaste_plain'),
                       url(r'^html/(?P<id>\d+)/$', 'html', name='djpaste_html'),)