from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
#from search.views import *
import os

site_media = os.path.join( os.path.dirname(__file__), 'site_media')
urlpatterns = patterns('',(r'^$','grandham.search.views.main_page'),
								  (r'^login/$', 'django.contrib.auth.views.login'),
		  (r'^search/$','grandham.search.views.search_page'),
		(r'^logout/$', 'grandham.search.views.logout_page'),
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': site_media}),
		  (r'^register/$','grandham.search.views.register_page'),
		  (r'^register/success/$', direct_to_template,{'template': 'registration/register_success.html'}),
		  (r'^ajax/title/autocomplete/$', 'grandham.search.views.ajax_title_autocomplete'),
		  (r'^ajax/author/autocomplete/$','grandham.search.views.ajax_author_autocomplete'),
		(r'^credits/$','grandham.search.views.credits'),
		(r'^chooseddc/$','grandham.search.views.choose_ddc'),
		(r'^biblio/$','grandham.search.views.biblio'),
		(r'^about/$','grandham.search.views.about_page'),
		(r'^license/$','grandham.search.views.license'),
) 
