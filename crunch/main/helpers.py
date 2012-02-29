import requests
import re
import sys
import simplejson
import csv
from django.db.models.fields import FieldDoesNotExist
from django.db import models
from crunch.main.models import Company
from main.models import Company, tag, ipo, financial_org, investments, funding_rounds, person, acquisition


# Calculates the amount raised for a given company by iterating over funding rounds.
def calc_amount_raised(company):
	
	co = company
	#initiate the funding
	amount_raised = 0
	
	try:
		
		for roundi in co.funding_rounds.all():
			
			raised = roundi.raised_amount
			#If the funding round was in euros we have to turn the amount into dollars:
			if roundi.raised_currency_code == 'EUR':
				raised = raised * 1.3
			
			amount_raised = amount_raised + raised
	except:
		pass

	return amount_raised

#Save all companies from cruncbase to db.
def save_all():
   
    url = 'http://api.crunchbase.com/v/1/companies.js'
    
    j = fetch_json(url)
    i =80917
    
    while (i < len(j)):
        print(j[i]['permalink'])
        if ((j[i]['permalink'] == 'it-martini') or 
            (j[i]['permalink'] == 'content-writing-india') or 
            (j[i]['permalink'] == 'tweriod') or 
            (j[i]['permalink'] == 'barspace') or 
            (j[i]['permalink'] == 'community-center-for-churches') or 
            (j[i]['permalink'] == 'agelio-networks') or
            (j[i]['permalink'] == 'synaptic-digital') or 
            (j[i]['permalink'] == 'planetlan') or
            (j[i]['permalink'] == 'startup-health') or
            (j[i]['permalink'] == 'autolime') or
            (j[i]['permalink'] == 'kiwi-commons') or
            (j[i]['permalink'] == 'kibm-daksh-it-company') or
            (j[i]['permalink'] == 'hitforkid') or
            (j[i]['permalink'] == 'raw-engineering') or
            (j[i]['permalink'] == 'the-feiwritz-group') or
            (j[i]['permalink'] == 'cornerblue')):
            i = i+1
            continue
        else:
            save_by_permalink(j[i]['permalink'])
            i = i+1
    

#Save a company when given a permalink
def save_by_permalink(permalink):
    
    #Get the url for the json
    url = co_url_by_p(permalink)
    
    #Get the json
    j = fetch_json(url)
    
    #Save the company from the json file fetched
    if j is not None or "error" not in j:
        save_straight(j)
    
def fetch_json(url):
    
    if not url:
        print('no url to helpers.fetch_json?')
        return
        
    #fetch the page defined in the argument url 
    r = requests.get(url)
    # We extract the contents
    c = r.content
    # And load the json into a python dict
    try:
        j = simplejson.loads(c)
    except:
        print('JSONDecodeError') 
        j = None
    
    # And return the dict
    return j
def co_url_by_p(p):
    
    url = 'http://api.crunchbase.com/v/1/company/'+ p +'.js'
    
    print(url)
    
    return url
    
def save_straight(dicta):
   
    p = dicta['permalink']

    try:
        co = Company.objects.get(permalink=p)
        return
    #if the company doesn't already exist, create it.
    except Company.DoesNotExist:
        print("This company doesn't exist")
        createCompany(dicta)

def createCompany(dicta):
    newco = Company()
    #start by creating the required fields
    
    #name
    newco.name = dicta["name"]
    #permalink
    try:
        newco.permalink = dicta["permalink"]
    except KeyError:
        newco.permalink
    #category_code
    newco.category_code = dicta["category_code"]
    #number of employees
    newco.number_of_employees = dicta["number_of_employees"]
    #founded year
    newco.founded_year = dicta["founded_year"]
    #founded_month
    newco.founded_month = dicta["founded_month"]
    #deadpooled_year
    newco.deadpooled_year = dicta["deadpooled_year"]
    #deadpooled_month
    newco.deadpooled_month = dicta["deadpooled_month"]
    #deadpooled_url
    newco.deadpooled_url = dicta["deadpooled_url"]
    #description
    newco.description = dicta["description"]
    #overview
    newco.overview = dicta["overview"]
    #total_money_raised
    newco.total_money_raised = dicta["total_money_raised"]
    
    #save to database before adding manytomanyfields
    newco.save()
    
    #Creating ManyToManyField values
    #ipo
    if dicta["ipo"] is not None:
        ipo1 = ipo()
        ipo1.valuation_amount = dicta["ipo"]["valuation_amount"]
        ipo1.valuation_currency_code = dicta["ipo"]["valuation_currency_code"]
        ipo1.pub_year = dicta["ipo"]["pub_year"]
        ipo1.pub_month = dicta["ipo"]["pub_month"]
        ipo1.pub_day = dicta["ipo"]["pub_day"]
        ipo1.stock_symbol = dicta["ipo"]["stock_symbol"]
        ipo1.save()
        newco.ipo.add(ipo1)
    else:
        print("ipo is null")
    
    #Creating funding rounds
    #Funding rounds require investments
    #Investments require either a company, financial_org or person
    # We iterate over the funding rounds, and inside the funding rounds iterate over investments. 
    if dicta["funding_rounds"] is not None:
        #Loop over funding rounds, create the funding round
        for f in dicta['funding_rounds']:
            fr = funding_rounds()
            fr.round_code = f['round_code']
            fr.raised_amount = f['raised_amount']
            fr.raised_currency_code = f['raised_currency_code']
            fr.funded_year = f['funded_year']
            fr.funded_month = f['funded_month']
            fr.funded_day = f['funded_day']
            fr.save()
            #In the current funding round, loop over the investments
            if f["investments"] is not None:
                inv = investments()
                inv.save()
                for i in f['investments']:
                    
                    # For company, financial_org and person, get or create the instance and add it to this investment
                    if i['company'] is not None:
                        try:
                            co = Company.objects.get(name=i['company']['name'])
                            inv.company.add(co)
                        #if the company doesn't already exist, create it.
                        except Company.DoesNotExist:
                            #Try to find the company's real crunchbase page
                            try:
                                permalink = i['company']['permalink']
                                save_by_permalink(permalink)
                                co = Company.objects.get(name=i['company']['name'])
                                inv.company.add(co)
                            except:
                                nCo, created = Company.objects.get_or_create(name=i['company']['name'])
                                inv.company.add(nCo)
                    if i['financial_org'] is not None:
                        try:
                            co = financial_org.objects.get(name=i['financial_org']['name'])
                            inv.financial_org.add(co)
                        #if the company doesn't already exist, create it.
                        except financial_org.DoesNotExist:
                            nCo, created = financial_org.objects.get_or_create(name=i['financial_org']['name'], permalink=i['financial_org']['permalink'])
                            inv.financial_org.add(nCo)
                    if i['person'] is not None:
                        try:
                            co = person.objects.get(permalink=i['person']['permalink'])
                            inv.person.add(co)
                        #if the company doesn't already exist, create it.
                        except person.DoesNotExist:
                            nCo, created = person.objects.get_or_create(first_name=i['person']['first_name'], last_name = i['person']['last_name'], permalink=i['person']['permalink'])
                            inv.person.add(nCo)
                #Add this investment thing in this funding round
                fr.investments.add(inv)
            #Add this funding round to the company
            newco.funding_rounds.add(fr)
    
    #tag_list
    
    if dicta['tag_list'] is not None or "":
    
        #turn the csv list into a list and then loop throught it
        #csv_to_list creates a list of the csv with tags
        taglist = csv_to_list(dicta['tag_list'])
        
        #loop through the list and add them as tags
        
        for i in taglist:
            try:
                tagi = tag.objects.get(tag = i)
                newco.tag_list.add(tagi)
            except tag.DoesNotExist:
                tagi = tag()
                tagi.tag = i
                tagi.save()
                newco.tag_list.add(tagi)
def add_acq(company, cb_json):
    
    dicta = cb_json

    try:
        if dicta['acquisition'] is not None or "":
            a = acquisition()
            a.price_amount = dicta["acquisition"]["price_amount"]
            a.price_currency_code = dicta["acquisition"]["price_currency_code"]
            a.term_code = dicta["acquisition"]["term_code"]
            a.source_url = dicta["acquisition"]["source_url"]
            a.source_description = dicta["acquisition"]["source_description"]
            a.acquired_year = dicta["acquisition"]["acquired_year"]
            a.acquired_month = dicta["acquisition"]["acquired_month"]
            a.acquired_day = dicta["acquisition"]["acquired_day"]
        
            if dicta['acquisition']['acquiring_company'] is not None:
                try:
                    co = Company.objects.get(name=dicta['acquisition']['acquiring_company']['name'])
                    a.acquiring_company = co
                    #if the company doesn't already exist, create it.
                except Company.DoesNotExist:
                    #Try to find the company's real crunchbase page
                    try:
                        permalink = dicta['acquisition']['acquiring_company']['permalink']
                        save_by_permalink(permalink)
                        co = Company.objects.get(name=dicta['acquisition']['acquiring_company']['name'])
                        a.acquiring_company = co
                    except:
                        nCo, created = Company.objects.get_or_create(name=dicta['acquisition']['acquiring_company']['name'])
                        nCo.permalink = dicta['acquisition']['acquiring_company']['permalink']
                        nCo.save()
                        a.acquiring_company = nCo
                a.save()
            try:
                company.acquisition = a
                print('added acquisition to company')
                company.save()
                print('saved it')
            except:
                ("couldn't add or save the acquisition")
    except:
        print('json sucked for' + str(company))
        

def csv_to_list(strik):
        
    taglist = [x.strip() for x in strik.split(',')]
    return taglist


# Recursive method that almost works, but doesn't.
def save_dict_to_db_R(model_class ,dicta):
    
    name = "name"
    print( 'dicta ' + str(dicta))
    print('model_class: ' + str(model_class))
    
    testCo = model_class()
    
    for key,value in dicta.items():
        try:
            field = model_class._meta.get_field(key)
            
            if isinstance(field, models.ManyToManyField):
                print("Found a ManyToManyField..." + field.name)
                continue
            else:
                if model_class._meta.get_field(key):
                    print("i == something:" + key + " ")
                    setattr(testCo, key, value)
        except FieldDoesNotExist:
            continue
            
    testCo.save()
    print('Saved: ' + str(testCo))
    print(' with id: ' + str(testCo.id))
    
    for field in model_class._meta.many_to_many:
        print("In the for loop: " + field.name)
        
        #if field.name in dicta:
        if field.name in dicta and hasattr(dicta[field.name], 'append'):
            print('field.name: ' + field.name)
            if dicta[field.name] is None:
                continue
            else:
                for obj in dicta[field.name]:
                    print('field.rel.to: ' + str(field.rel.to))
                    print('object: ' + str(obj))
                    rel_instance = save_dict_to_db_R(field.rel.to, obj)
                    #for (key, val) in field:
                    #   print('key: '+ key + ' val: ' + val)
                    print(str(rel_instance))
                    if rel_instance is None:
                        print('rel_instance is None')
                        continue
                    else:
                        getattr(testCo, field.name).add(rel_instance)
                        print('adding' + field.name + ' : ' + rel_instance)
                    print(rel_instance)
        
   
#The original recursive one that was copied. Something fucks up.
def create_or_update_and_get(model_class, data):
    get_or_create_kwargs = {
        model_class._meta.pk.name: data.pop(model_class._meta.pk.name)
    }
    try:
        # get
        instance = model_class.objects.get(**get_or_create_kwargs)
    except model_class.DoesNotExist:
        # create
        instance = model_class(**get_or_create_kwargs)
    # update (or finish creating)
    for key,value in data.items():
        field = model_class._meta.get_field(key)
        if not field:
            continue
        if isinstance(field, models.ManyToManyField):
            # can't add m2m until parent is saved
            continue
        elif isinstance(field, models.ForeignKey) and hasattr(value, 'items'):
            rel_instance = create_or_update_and_get(field.rel.to, value)
            setattr(instance, key, rel_instance)
        else:
            setattr(instance, key, value)
    instance.save()
    # now add the m2m relations
    for field in model_class._meta.many_to_many:
        if field.name in data and hasattr(data[field.name], 'append'):
            for obj in data[field.name]:
                rel_instance = create_or_update_and_get(field.rel.to, obj)
                getattr(instance, field.name).add(rel_instance)
    return instance


def parse_tag(self, tag_list):
    mylist =[]
    reader = csv.reader(tag_list, skipinitialspace=True)
    for r in reader:
        mylist.append(r)
        
    return mylist
        
    