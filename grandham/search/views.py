# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from grandham.search.forms import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from grandham.search.models import *
import string as mod_string
r=1
value=""

def ajax_title_autocomplete(request):
	if 'q' in request.GET:
		title=Title_word.objects.filter(word__istartswith=request.GET['q'])[:100]
		return HttpResponse(unicode('\n'.join([words.word for words in title])))

def ajax_author_autocomplete(request):
	if 'q' in request.GET:
		title=Author.objects.filter(Author__istartswith=request.GET['q'])[:100]
		return HttpResponse(unicode('\n'.join([words.Author for words in title])))

#Static pages
def main_page(request):
	return render_to_response('main_page.html',RequestContext(request))
	
def license(request):
	return render_to_response('license.html',[])

def credits(request):
        return render_to_response('credits.html',RequestContext(request))

def about_page(request):
	return render_to_response('about.html',[])

#Registration and related pages
def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
			return HttpResponseRedirect('/register/success')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('registration/register.html',variables)

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')

#Search related pages
def search_page(request):
	ddc = []
	ids_search=[]
	for i in DDC.objects.all():
		ddc.append((i.DDC,i.subject))
	if request.method == 'POST' :
		form=SearchForm(request.POST)
		results=[]
		value=""		
		for i in DDC.objects.all():
			if i.subject==form.data['ddc']:
				value=i.DDC
		k=1
		for i in Book.objects.filter(Title__icontains=unicode(form.data['title']),Author__icontains=unicode(form.data['author']),DDC__istartswith=unicode(value)):
			results.append((k,i.Title,i.Author,i.Year))
			ids_search.append(i.id)
			k=k+1
		variables = RequestContext(request,{'form': form,'show_results': True,'results':results,'ddc':ddc,'ids_search':ids_search})
	else:
		form=SearchForm()
		variables = RequestContext(request,{'form': form,'ddc':ddc})
	return render_to_response('search_page.html',variables)

def choose_ddc(request):
	global r,value
	r=0
	if 'ddc1' in request.POST.keys():
		ddc = []
		val=request.POST['ddc1'].split(",")[0].split("'")[1]
		for i in DDC.objects.all():
			ddc.append((i.DDC,i.subject))
			if i.DDC==val:
				value=i.subject
		return render_to_response('search_page.html',RequestContext(request,{'form':SearchForm(),'setddc':True,'ddc':ddc,'val':value}))
	else:		
		return search_page(request)

def biblio(request):
	list= request.POST['book'].replace(")","").replace("(","").replace("u'","").replace("'","").split(",")[0]
	ids_list=request.POST['ids_search'].replace("[","").replace("]","").replace("u'","").replace("L","").replace("'","").split(", ")
	result=Book.objects.filter(id=int(ids_list[int(list)-1]).__str__())	
	k=DDC.objects.filter(DDC=result.values_list()[0][2]).values_list()[0][2]	
	variables = RequestContext(request,{'list':result[0],'subject':k})
	return render_to_response('biblio.html',variables)


