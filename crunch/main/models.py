from django.db import models

# Create your models here.
class Company(models.Model):
    #name
    name = models.CharField(max_length=100, null=True, blank=True)
    #permalink
    permalink = models.CharField(max_length=100, null=True, blank=True)
    #category_code
    category_code = models.CharField(max_length=100, null=True, blank=True)
    #number of employees
    number_of_employees = models.IntegerField(null=True)
    #founded year
    founded_year = models.IntegerField(null=True)
    #founded_month
    founded_month = models.IntegerField(null=True)
    #deadpooled_year
    deadpooled_year = models.IntegerField(null=True)
    #deadpooled_month
    deadpooled_month = models.IntegerField(null=True)
    #deadpooled_url
    deadpooled_url = models.URLField(null=True)
    #tag_list
    tag_list = models.ManyToManyField("tag", null =True, related_name = "Company_tag")
    #description
    description = models.TextField(null=True, blank=True)
    #overview
    overview = models.TextField(null=True, blank=True)
    #total_money_raised
    total_money_raised = models.CharField(max_length=100,null=True, blank=True)
    #funding_rounds
    funding_rounds = models.ManyToManyField("funding_rounds", null=True, related_name = "Company_fr")
    #ipo
    ipo = models.ManyToManyField("ipo", null=True, related_name ="Company_ipo")
    
    #exit
    acquisition = models.OneToOneField("acquisition", null=True, related_name="Exit")
    
    def get_fields(self):
        return [(field, field.value_to_string(self)) for field in Company._meta.fields]
    
    def __unicode__(self):
        return self.name
#If it has been acquired
class acquisition(models.Model):
    price_amount = models.IntegerField(null=True)
    price_currency_code = models.CharField(max_length=10, null=True, blank=True)
    term_code = models.CharField(max_length=40, null=True, blank=True)
    source_url= models.URLField(null=True, blank=True)
    source_description = models.TextField(null=True)
    acquired_year = models.IntegerField(null=True)
    acquired_month = models.IntegerField(null=True)
    acquired_day = models.IntegerField(null=True)
    acquiring_company = models.ForeignKey("Company", null=True, related_name="acquisitions")
    
    def __unicod__(self):
        return u'%s %s' % (self.acquisition, self.price_amount, self.acquiring_company)
    
class tag(models.Model):
    tag = models.CharField(max_length = 100, null=True, blank=True)
    
    def __unicode__(self):
        return self.tag
#ipo        
class ipo(models.Model):
    valuation_amount = models.IntegerField(null = True)
    valuation_currency_code = models.CharField(max_length=20, null=True, blank=True)
    pub_year = models.IntegerField(null=True)
    pub_month = models.IntegerField(null=True)
    pub_day = models.IntegerField(null=True)
    stock_symbol = models.CharField(max_length=30, null=True, blank=True)

    def __unicode__(self):
        return self.stock_symbol
#funding rounds
class funding_rounds(models.Model):
    round_code = models.CharField(max_length=20, null=True, blank=True)
    raised_amount = models.IntegerField(null=True)
    raised_currency_code = models.CharField(max_length=20, null=True, blank=True)
    funded_year = models.IntegerField(null=True)
    funded_month = models.IntegerField(null=True)
    funded_day = models.IntegerField(null=True)
    investments = models.ManyToManyField("investments", null=True)
    
    def __unicode__(self):
        return self.round_code

class investments(models.Model):
    company = models.ManyToManyField("Company", null=True, related_name ="Investments_company")
    financial_org = models.ManyToManyField("financial_org", null=True, related_name ="Investments_financial_org")
    person = models.ManyToManyField("person", null=True, related_name ="Investments_person")
    
class financial_org(models.Model):
    name = models.CharField(max_length = 100, null=True, blank=True)
    permalink = models.CharField(max_length = 100, null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class person(models.Model):
    first_name = models.CharField(max_length = 100, null=True, blank=True)
    last_name = models.CharField(max_length = 100, null=True, blank=True)
    permalink = models.CharField(max_length = 100, null=True, blank=True)
    
    def __unicode__(self):
        return self.permalink

#funding rounds


#[round_code
#raised_amount
#raised_currency_code
#funded_year
#funded_month
#funded_day

#investments
#[financial_org (multiple)
#person (multiple)]