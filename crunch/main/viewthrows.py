import requests
import sys
import simplejson
import csv
from django.db.models.fields import FieldDoesNotExist
from django.db import models
from crunch.main.models import Company
from main.models import Company, tag, ipo, financial_org, investments, funding_rounds, person, acquisition
from main.helpers import *
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

# by_tag_view returns a list of dicts for each company with the required attributes
# Required attributes: 
#
def by_tag_view(list_of_companies):

	codict_list = []
	print('in by_tag_view')
	
	for co in list_of_companies:
		
		#an empty dict which will be filled with the company attributes
		co_dict = {}
		round_dates = {}
		ipo = {'valuation': 0}
		acquisition = {'acquisition_amount': 0}
		
		name = co.name
		print('Printing co name:')
		print(name)
		description = co.description
		
		#Get total funding from helpers.py calc_amount_raised
		amount_raised = calc_amount_raised(co)
		
		try:
			
			for roundi in co.funding_rounds.all():

				round_dates = {'code': roundi.round_code, 'month': roundi.funded_month, 'year': roundi.funded_year}
				print(round_dates)
		except: 
			print('exception in round_dates in by_tag_view')
		
		try:
			for ipo in co.ipo.all():
				if ipo.valuation_amount is None:
					ipo.valuation_amount = 0
				amount = ipo.valuation_amount
				ipo = {'symbol': ipo.stock_symbol, 'valuation': amount , 'month': ipo.pub_month, 'year': ipo.pub_year}
		except: 
			print('exception in ipo in by_tag_view')
			
		
		try:
			price = co.acquisition.price_amount
		
			if co.acquisition.price_currency_code == 'EUR':
				price = price * 1.3
			
			acquisition = {'acquisition_amount': price, 'month': co.acquisition.acquisition_month, 
							'year': co.acquisition.acquisition_year}
		except: 
			print('exception in acquisition in by_tag_view')
		
		co_dict = {'name': name, 'description': description, 'amount_raised': amount_raised, 
					'round_dates': round_dates, 'ipo': ipo, 'acquisition': acquisition}
		
		codict_list.append(co_dict)
		print(codict_list)
		
	return codict_list
				
		
	
