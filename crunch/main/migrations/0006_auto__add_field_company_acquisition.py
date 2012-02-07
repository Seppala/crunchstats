# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Company.acquisition'
        db.add_column('main_company', 'acquisition', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Exit', unique=True, null=True, to=orm['main.acquisition']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Company.acquisition'
        db.delete_column('main_company', 'acquisition_id')


    models = {
        'main.acquisition': {
            'Meta': {'object_name': 'acquisition'},
            'acquired_day': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'acquired_month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'acquired_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'acquiring_company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'acquisitions'", 'null': 'True', 'to': "orm['main.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'price_currency_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'source_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'term_code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        'main.company': {
            'Meta': {'object_name': 'Company'},
            'acquisition': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Exit'", 'unique': 'True', 'null': 'True', 'to': "orm['main.acquisition']"}),
            'category_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'deadpooled_month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'deadpooled_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'deadpooled_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'founded_month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'founded_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'funding_rounds': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Company_fr'", 'null': 'True', 'to': "orm['main.funding_rounds']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Company_ipo'", 'null': 'True', 'to': "orm['main.ipo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number_of_employees': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'overview': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tag_list': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Company_tag'", 'null': 'True', 'to': "orm['main.tag']"}),
            'total_money_raised': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'main.financial_org': {
            'Meta': {'object_name': 'financial_org'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'main.funding_rounds': {
            'Meta': {'object_name': 'funding_rounds'},
            'funded_day': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'funded_month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'funded_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.investments']", 'null': 'True', 'symmetrical': 'False'}),
            'raised_amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'raised_currency_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'round_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
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
            'stock_symbol': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'valuation_amount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'valuation_currency_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'main.person': {
            'Meta': {'object_name': 'person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'main.tag': {
            'Meta': {'object_name': 'tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']
