from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from main.helpers import *
from main.Db_handling import *
from main.viewthrows import *
from main.models import Company

def home(request):
    #context = {'companies': Company.objects.all()}
    return render(request, 'home.html')

#returns the total money raised by companies
def raised_by_tag(request):
	if 'tag' in request.GET:
		#print(request.GET['tag'])
		message ='you searched for companies with the tag: %r' % request.GET['tag']
	else:
		message = "you searched empty..."
	
	tag = request.GET['tag']
	
	#get all companies that include that tag. returns a list of company objects
	cos = get_by_tag(tag)
	
	#turn the list of company objects into a list of dicts with the required attributes
	co_dictlist = by_tag_view(cos)
	
	
	
	#order the company list
	#co_sorted = sorted(co_dictlist, key=lambda d: (d['name']))
	co_sorted = sorted(co_dictlist, key=lambda d: (-d['ipo']['valuation'], -d['acquisition']['acquisition_amount'], 
						-d['amount_raised'], d['name']))
	#co_sorted = cos.sort(key=lambda x:(x['name']))
	
	return render_to_response('by_tag.html', {'companies': co_sorted, 'tag': tag}, context_instance=RequestContext(request))

#saves all the crunchbase companies to a database.
def save_crunchbase(request):
    save_all()
    companies = Company.objects.all()

    #return HttpResponse(message) 
    #render(request, 'home.html', context)
    return render_to_response('home.html',
            {'companies': companies}, context_instance=RequestContext(request))

def permalink_to_db(request):
    #p = permalink
    #put permalink in URL
    if 'permalink' in request.POST:
        message = 'You searched for: %r' % request.POST['permalink']
    else:
        message = 'You submitted an empty form.'
    permalink = request.POST['permalink']
    URL = 'http://api.crunchbase.com/v/1/company/' + permalink + '.js'
    
    #fetch the json
    try:
       j = fetch_json(URL)
        
    except ():
        return render_to_response(request, 'home.html', {
        'error_message': "That permalink was not valid! Or then I just screwed up...",},
        context_instance=RequestContext(request)
        )
        
    #Throw json to the correct function
    save_straight(j)

    companies = Company.objects.all()

    #return HttpResponse(message) 
    #render(request, 'home.html', context)
    return render_to_response('home.html',
            {'companies': companies, 'query': permalink}, context_instance=RequestContext(request))

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
    
def addacq(request):
	i = 24101
	#For all the companies in the db
	while i < len(Company.objects.all()):
	#while i < 50:
		co = Company.objects.get(pk=i)
		print(i)
		print(co)
		i=i+1
		
		cb_url = co_url_by_p(co.permalink)
	#for co in Company.objects.all():
		#fetch their CB url
	#	print(i)
	#	i = i+1
	#	cb_url = co_url_by_p(co.permalink)
		
		#fetch their json
		co_json = fetch_json(cb_url)
		
		#add the acq
		add_acq(co, co_json)
		
	return render_to_response('home.html',
		{'companies': Company.objects.all()}, context_instance=RequestContext(request))

def smallsociety(request):
	co = Company.objects.get(permalink = "saaspoint")
	
	acq = co.acquisition
	print(acq)
	return render_to_response('smallsociety.html', {'co': co, 'a' : acq}, context_instance=RequestContext(request))
		
		
    