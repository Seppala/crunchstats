import requests
import sys
import simplejson
import csv
from django.db.models.fields import FieldDoesNotExist
from django.db import models
from crunch.main.models import Company
from main.models import Company, tag, ipo, financial_org, investments, funding_rounds, person, acquisition
from main.helpers import *

# by_tag_view returns a list of dicts for each company with the required attributes
# Required attributes: 
#
def by_tag_view(list_of_companies):

	dict_list = []
	for co in list_of_companies:
		
		#an empty dict which will be filled with the company attributes
		co_dict = {}
		
		name = co.name
		description = co.description
		
		#turn the money raised into US dollars
		# '$200M'
		money = co.total_money_raised
		
		total_money_raised = dollar_strip(money)
		
		
	
