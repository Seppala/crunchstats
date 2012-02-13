"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test.client import Client
from django.test import TestCase
from main.models import Company, tag, ipo, financial_org, investments, funding_rounds, person, acquisition
from main.helpers import *
from main.Db_handling import *
from main.viewthrows import *
import requests
import simplejson

class TestCompanyModel(TestCase):
    def setUp(self):
        newco = Company()
        
        #start by creating the required fields
        
        #name
        newco.name = "SuperStartup"
        #permalink
        newco.permalink = "superstartup"
        #category_code
        newco.category_code ="software"
        #number of employees
        newco.number_of_employees = 3
        #founded year
        newco.founded_year = 2001
        #founded_month
        newco.founded_month = None
        #deadpooled_year
        newco.deadpooled_year = None
        #deadpooled_month
        newco.deadpooled_month = None
        #deadpooled_url
        #newco.deadpooled_url = ''
        
        #description
        newco.description = "newco makes widgets that automate productivity of efficient social features in the health, retail, industry, banking, telecommunications, construction and small business accounting industries"
        #overview
        newco.overview = "We are revolution to market"
        #total_money_raised
        newco.total_money_raised = "\u20ac183M"
        
        #save to database before adding manytomanyfields
        newco.save()
        
        #adding ManyToManyField values
        #ipo
        ipo1 = ipo()
        ipo1.save()
        newco.ipo.add(ipo1)
        
        #tag_list
        tag1 = tag(tag = "venture-capital-company")
        tag1.save()
        tag2 = tag(tag = "disruptive-technology-start-ups")
        tag2.save()
        
        newco.tag_list.add(tag1)
        newco.tag_list.add(tag2)

        #funding rounds
        #financial organization
        financial1 = financial_org()
        financial1.name = "Open Ocean"
        financial1.permalink = "openocean"
        financial1.save()
        #investment
        investment1 = investments()
        investment1.save()
        investment1.financial_org.add(financial1)
        
        #round
        round1 = funding_rounds()
        round1.round_code = "a"
        round1.raised_amount = 21640000 
        round1.raised_currency_code = "EUR"
        round1.funded_year = 2008 
        round1.funded_month = 10 
        round1.funded_day = 30 
        round1.save()
        print("Saved the easy funding round...")
        round1.investments.add(investment1)
        
        #Add the funding round
        newco.funding_rounds.add(round1)

    def get_json_doesnt_exist(self):
        url = 'http://api.crunchbase.com/v/1/company/qestu.js'
        
        j = fetch_json(url)
        
        name = j['name']

    def test_by_tag_view(self):
        all_cos = Company.objects.all()
        co = all_cos[0]
        
        co_list = []
        
        co_list.append(co)
        
        print ('Printing co_list:')
        print co_list
        
        nyy_list = by_tag_view(co_list)
        
        print('Printing the list I got back:')
        print nyy_list

    def test_creating_a_new_company_with_name_and_permalink(self):
        
        #[round_code
        #raised_amount
        #raised_currency_code
        #funded_year
        #funded_month
        #funded_day

        #investments
        #[financial_org (multiple)
        #person (multiple)]
        #ipo

        #Check that we can find newco it in the database

        all_companies_in_database = Company.objects.all()
        self.assertEquals(len(all_companies_in_database), 1)
        only_company_in_database = all_companies_in_database[0]
        self.assertEquals(only_company_in_database.name, "SuperStartup")

        #Check that the attributes are saved correctly
        self.assertEquals(only_company_in_database.name, "SuperStartup")
        self.assertEquals(only_company_in_database.permalink, "superstartup")
        
        #category_code
        self.assertEquals(only_company_in_database.category_code, "software")
        #number of employees
        self.assertEquals(only_company_in_database.number_of_employees, 3)
        #founded year
        self.assertEquals(only_company_in_database.founded_year, 2001)
        #founded_month
        self.assertEquals(only_company_in_database.founded_month, None)
        #deadpooled_year
        self.assertEquals(only_company_in_database.deadpooled_year, None)
        #deadpooled_month
        self.assertEquals(only_company_in_database.deadpooled_month, None)
        #deadpooled_url
        self.assertEquals(only_company_in_database.deadpooled_url, None)
        #tag_list
        
        self.assertEquals(only_company_in_database.tag_list.get(id=1).tag, "venture-capital-company")
        self.assertEquals(only_company_in_database.tag_list.get(id=2).tag, "disruptive-technology-start-ups")
        #description
        self.assertEquals(only_company_in_database.description, "newco makes widgets that automate productivity of efficient social features in the health, retail, industry, banking, telecommunications, construction and small business accounting industries")
        #overview
        self.assertEquals(only_company_in_database.overview, "We are revolution to market")
        #total_money_raised
        self.assertEquals(only_company_in_database.total_money_raised, "\u20ac183M")
        #ipo
        #self.assertEquals(only_company_in_database.ipo.get(id=1), ipo1)
        
        
        #funding rounds
        #self.assertEquals(only_company_in_database.funding_rounds.get(id=1), round1)
        #[round_code
        #raised_amount
        #raised_currency_code
        #funded_year
        #funded_month
        #funded_day

        #investments
        #[financial_org (multiple)
        #person (multiple)]
        
    def test_company_objects_are_named_as_their_name(self):
        p = Company()
        p.name = "Qestu"
        self.assertEquals(unicode(p), 'Qestu')

    def test_add_acquisition(self):
        co = Company()
        
        #start by creating the required fields
        
        #name
        co.name = "SuperStartup"
        print('added superstartup in test_add_acquisition')
        #permalink
        co.permalink = "superstartup"

        url = 'http://api.crunchbase.com/v/1/company/m5-networks-3.js'
        dicta = fetch_json(url)
        
        #all_companies_in_database = Company.objects.all()
        #self.assertEquals(len(all_companies_in_database), 1)
        #co = all_companies_in_database[0]
        self.assertEquals(co.name, "SuperStartup")
        
        print(co)
        #Add the acquisition from the json to the 
        add_acq(co, dicta)
        #a = acquisition()
        #a.term_code ='shares'
        #co.acquisition = a
        
        print('Acquisition term code: ' + co.acquisition.term_code)
       
        #co = all_companies_in_database[0]
        name = co.name
        
        acq_code = co.acquisition.term_code
        
        self.assertEquals('cash_and_stock', acq_code)
        self.assertEquals('shoretel', co.acquisition.acquiring_company.permalink)

        
        
class TestHelpers(TestCase):
    
    def test_csv_to_list(self):
        my_string = "raaka, joku, joo"
        lista = csv_to_list(my_string)
        listTest = ["raaka", "joku", "joo"]
        
        self.assertEquals(lista, listTest)  
        
class TestJsons(TestCase):
    
    #test if you can get the length of the json
    def test_len(self):
        url = 'http://api.crunchbase.com/v/1/companies.js'

        j = fetch_json(url)

        print('companies: ' + str(len(j)))
    # Test if you get the right companies from companies.js the three companies 
    def test_fetching_three_cos_from_companiesjs(self):
        
        url = 'http://api.crunchbase.com/v/1/companies.js'
        
        j = fetch_json(url)
        
        i=0
        
        while (i < 4):
            print(j[i]['permalink'])        
            save_by_permalink(j[i]['permalink'])
            i = i+1
            
        all = Company.objects.all()
        self.assertEquals(len(all), 4)
        print(all)

        wetpaint = Company.objects.get(pk=1)
        print(wetpaint)
        self.assertEquals(wetpaint.permalink, 'wetpaint')
        self.assertEquals(Company.objects.get(pk=2).permalink, 'adventnet')
        self.assertEquals(Company.objects.get(pk=3).permalink, 'zoho')
        self.assertEquals(Company.objects.get(pk=4).permalink, 'digg')
        

            
    
    def test_fetching_json(self, url = ''):
        # First, we get a json file
        if not url:
            url = 'http://api.crunchbase.com/v/1/person/patrik-backman.js'
        
        r = requests.get(url)
        # We extract the contents
        print(url)
        c = r.content
        # And load the json into a python dict
        j = simplejson.loads(c)

        # We check that the json is what we wanted it to be. Here we check that the first name corresponds to 
        # what we should get from the json
        self.assertEquals(j["first_name"], "Patrik")
        
        return j

    def test_fetching_and_saving_json(self):
        
        #get company url by permalink
        p = 'spotify'

        url = co_url_by_p(p)
        
        #Use this to test the helpers function directly (uncomment save_straight(j))
        
        j = fetch_json(url)
        print('And the funding round is... :' + j['funding_rounds'][0]['round_code'])
        
        save_straight(j)

        
        # Check that the company has been correctly saved in the database as the first company with the
        # right name and permalink
        all_companies_in_database = Company.objects.all()
        self.assertEquals(len(all_companies_in_database), 1)
        only_company_in_database = all_companies_in_database[0]

        #self.assertEquals(only_company_in_database, testCo)

        #Check that the attributes are saved correctly
        self.assertEquals(only_company_in_database.name, "Spotify")
        

        #name
        self.assertEquals(only_company_in_database.name, "Spotify")
        #permalink
        self.assertEquals(only_company_in_database.permalink, "spotify")
        #category_code
        self.assertEquals(only_company_in_database.category_code, "web")
        #number of employees
        self.assertEquals(only_company_in_database.number_of_employees, 200)
        #founded year
        self.assertEquals(only_company_in_database.founded_year, 2009)
        #founded_month
        self.assertEquals(only_company_in_database.founded_month, 12)
        #deadpooled_year
        self.assertEquals(only_company_in_database.deadpooled_year, None)
        #deadpooled_month
        self.assertEquals(only_company_in_database.deadpooled_month, None)
        #deadpooled_url
        self.assertEquals(only_company_in_database.deadpooled_url, None)
        
        #description
        self.assertEquals(only_company_in_database.description, "Music streaming")

        #overview
        print('overview: ' + only_company_in_database.overview)
        #total_money_raised
        self.assertEquals(only_company_in_database.total_money_raised, "$183M")
       
        #ipo
        self.assertEquals(only_company_in_database.ipo.count(), 0)
        
        #tag_list
        print(dir(only_company_in_database.tag_list))
        self.assertEquals(only_company_in_database.tag_list.count(), 4)

        #funding rounds
        #financial organization
        print(only_company_in_database.funding_rounds.count())
        print('Only Company Round pk=1: ')
        print('Only Company Round pk=1: ' + str(only_company_in_database.funding_rounds.get(pk=1)))
        a_round = only_company_in_database.funding_rounds.get(round_code="a")
        investment = a_round.investments.get(pk=1)
        fin_org = investment.financial_org
        self.assertEquals(fin_org.get(pk=1).permalink, "creandum")
             
        #investment
        #round2
        b_round = only_company_in_database.funding_rounds.get(round_code="b")
        self.assertEquals(b_round.raised_amount, 50000000)
        self.assertEquals(b_round.funded_year, 2009)

        all_companies_in_database = Company.objects.all()
        self.assertEquals(len(all_companies_in_database), 1)
        only_company_in_database = all_companies_in_database[0]
        self.assertEquals(only_company_in_database, Company.objects.get(pk=1))

        Spotify = Company.objects.get(permalink = 'spotify')
        print('in get_total_money.. Spotify is:' + Spotify.name)
        tm = calc_raised(Spotify)

        print('Spotify has raised:' + str(tm))
        print('total money raised' + Spotify.total_money_raised)

        cuus = get_by_tag('cloud')
        print('gotten by get_by_tag:')
        print(cuus)
        

#This test didn't work
    def get_total_money(self):
    
        all_companies_in_database = Company.objects.all()
        self.assertEquals(len(all_companies_in_database), 1)
        only_company_in_database = all_companies_in_database[0]

        #self.assertEquals(only_company_in_database, testCo)

        #Check that the attributes are saved correctly
        self.assertEquals(only_company_in_database.name, "Spotify")
        

        #name
        self.assertEquals(only_company_in_database.name, "Spotify")
        #permalink
        self.assertEquals(only_company_in_database.permalink, "spotify")

        print ('permalink is: ' + only_company_in_database.permalink)
        
        Spotify = Company.objects.get(permalink = 'spotify')
        print('in get_total_money.. Spotify is:' + Spotify)
        tm = calc_raised(Spotify)

        print('Spotify has raised:' + tm )
            
class TestHomePageView(TestCase):
    def root_url_shows_all_companies(self):
        company1 = Company(name='Boring Company', permalink='boringcompany')
        company1.save()
        company2 = Company(name='Exciting Company', permalink='excitingcompany')
        company2.save()
        
        client = Client()
        response = client.get('/')
        
        template_names_used = [t.name for t in response.templates]
        self.assertIn('home.html', template_names_used)
        
        #Check we've passed the companies to the template
        companies_in_context = response.context['companies']
        self.assertEquals(list(companies_in_context), [company1, company2])
        
        #Check that the company names appear on the page
        
        self.assertIn(company1.name, response.content)
        self.assertIn(company2.name, response.content)
        
class TestViewing(TestCase):

    def get_total_money(self):
        Spotify = Company.objects.get(permalink = 'spotify')
        print('in testviewing.. Spotify is:' + Spotify)
        tm = calc_raised(Spotify)

        print('Spotify has raised:' + tm )


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
