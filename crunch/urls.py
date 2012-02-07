from django.conf.urls.defaults import patterns, include, url
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
	(r'^search/$', views.search),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
