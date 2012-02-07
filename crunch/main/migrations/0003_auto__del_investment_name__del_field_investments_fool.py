# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Investment_name'
        db.delete_table('main_investment_name')

        # Deleting field 'investments.fool'
        db.delete_column('main_investments', 'fool')


    def backwards(self, orm):
        
        # Adding model 'Investment_name'
        db.create_table('main_investment_name', (
            ('person', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('financial_org', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['Investment_name'])

        # Adding field 'investments.fool'
        db.add_column('main_investments', 'fool', self.gf('django.db.models.fields.CharField')(default='jappa', max_length=20), keep_default=False)


    models = {
        'main.company': {
            'Meta': {'object_name': 'Company'},
            'category_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'deadpooled_month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'deadpooled_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'deadpooled_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'founded_month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'founded_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'funding_rounds': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Company_fr'", 'null': 'True', 'to': "orm['main.funding_rounds']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Company_ipo'", 'null': 'True', 'to': "orm['main.ipo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_of_employees': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tag_list': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Company_tag'", 'null': 'True', 'to': "orm['main.tag']"}),
            'total_money_raised': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.financial_org': {
            'Meta': {'object_name': 'financial_org'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.funding_rounds': {
            'Meta': {'object_name': 'funding_rounds'},
            'funded_day': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'funded_month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'funded_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.investments']", 'null': 'True', 'symmetrical': 'False'}),
            'raised_amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'raised_currency_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'round_code': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.investments': {
            'Meta': {'object_name': 'investments'},
            'company': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Investments_company'", 'null': 'True', 'to': "orm['main.Company']"}),
            'financial_org': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Investments_financial_org'", 'null': 'True', 'to': "orm['main.financial_org']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Investments_person'", 'null': 'True', 'to': "orm['main.person']"})
        },
        'main.ipo': {
            'Meta': {'object_name': 'ipo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_day': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pub_month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pub_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'stock_symbol': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'valuation_amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'valuation_currency_code': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.person': {
            'Meta': {'object_name': 'person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.tag': {
            'Meta': {'object_name': 'tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']
