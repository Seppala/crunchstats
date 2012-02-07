from main.models import Company, tag, ipo, funding_rounds, investments, financial_org, person, acquisition
from django.contrib import admin

class CompanyAdmin(admin.ModelAdmin):
    search_field = ['name']

admin.site.register(Company, CompanyAdmin)
admin.site.register(tag)
admin.site.register(ipo)
admin.site.register(funding_rounds)
admin.site.register(investments)
admin.site.register(financial_org)
admin.site.register(person)
admin.site.register(acquisition)