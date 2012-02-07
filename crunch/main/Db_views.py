import requests
import sys
import simplejson
import csv
from django.db.models.fields import FieldDoesNotExist
from django.db import models
from crunch.main.models import Company
from main.models import Company, tag, ipo, financial_org, investments, funding_rounds, person
