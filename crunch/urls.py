from django.conf.urls.defaults import patterns, include, url
from settings import *
from crunch.main import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   
    # homepage
	url(r'^$', views.home),
	
	#pull all companies to db
	url(r'^run/$', views.save_crunchbase),
	
	url(r'^by_tag/$', views.raised_by_tag),
	
	#add acquisitions
	url(r'^addacq/$', views.addacq),
	
	#Smallsociety test page
	url(r'^small/$', views.smallsociety),
	
	#Get companies 
	#Test for a form
	url(r'^search/$', views.search),
	
	#Could be useful
	#if settings.DEBUG:
	#    urlpatterns += patterns('',
	#        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
	#)
	
	#Media urls
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
	{'document_root': settings.MEDIA_ROOT }),
	
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
