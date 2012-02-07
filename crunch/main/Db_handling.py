import requests
import sys
import simplejson
import csv
from django.db.models.fields import FieldDoesNotExist
from django.db import models
from crunch.main.models import Company
from main.models import Company, tag, ipo, financial_org, investments, funding_rounds, person

def calc_raised(co_obj):
    
    # For the given company object, get the list of funding rounds
    fr = co_obj.funding_rounds.all()
    
    # Initialize amount to 0
    a = 0
    
    for i in fr:
        a = a + i.raised_amount
    
    return a
    
def get_by_tag(given_tag):
    
    #get all companies
    cos = Company.objects.all()
    
    #create an empty list
    tag_cos = []
    #loop through all the cos
    for c in cos:
    
        #get the tag list for the company
        t_list = c.tag_list.all()
        #loop through the tag list
        for t in t_list:
        
            #if the tag matches the given_tag, append the company to the list
            if given_tag in t.tag:
                tag_cos.append(c)
    
    return tag_cos

#Fetch all companies that have ipo'd
def get_ipos():
	cos = Company.objects.all()
	
	#create an empty list
	ipos = []
	
	#for c in cos:
		#get ipo for company
		
                    

            
        