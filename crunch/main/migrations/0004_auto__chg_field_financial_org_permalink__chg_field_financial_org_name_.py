# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'financial_org.permalink'
        db.alter_column('main_financial_org', 'permalink', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'financial_org.name'
        db.alter_column('main_financial_org', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'ipo.valuation_currency_code'
        db.alter_column('main_ipo', 'valuation_currency_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'ipo.stock_symbol'
        db.alter_column('main_ipo', 'stock_symbol', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'person.permalink'
        db.alter_column('main_person', 'permalink', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'person.last_name'
        db.alter_column('main_person', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'person.first_name'
        db.alter_column('main_person', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'funding_rounds.round_code'
        db.alter_column('main_funding_rounds', 'round_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'funding_rounds.raised_currency_code'
        db.alter_column('main_funding_rounds', 'raised_currency_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Company.category_code'
        db.alter_column('main_company', 'category_code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Company.permalink'
        db.alter_column('main_company', 'permalink', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Company.description'
        db.alter_column('main_company', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Company.overview'
        db.alter_column('main_company', 'overview', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Company.total_money_raised'
        db.alter_column('main_company', 'total_money_raised', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Company.name'
        db.alter_column('main_company', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'tag.tag'
        db.alter_column('main_tag', 'tag', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'financial_org.permalink'
        raise RuntimeError("Cannot reverse this migration. 'financial_org.permalink' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'financial_org.name'
        raise RuntimeError("Cannot reverse this migration. 'financial_org.name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'ipo.valuation_currency_code'
        raise RuntimeError("Cannot reverse this migration. 'ipo.valuation_currency_code' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'ipo.stock_symbol'
        raise RuntimeError("Cannot reverse this migration. 'ipo.stock_symbol' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'person.permalink'
        raise RuntimeError("Cannot reverse this migration. 'person.permalink' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'person.last_name'
        raise RuntimeError("Cannot reverse this migration. 'person.last_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'person.first_name'
        raise RuntimeError("Cannot reverse this migration. 'person.first_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'funding_rounds.round_code'
        raise RuntimeError("Cannot reverse this migration. 'funding_rounds.round_code' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'funding_rounds.raised_currency_code'
        raise RuntimeError("Cannot reverse this migration. 'funding_rounds.raised_currency_code' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Company.category_code'
        raise RuntimeError("Cannot reverse this migration. 'Company.category_code' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Company.permalink'
        raise RuntimeError("Cannot reverse this migration. 'Company.permalink' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Company.description'
        raise RuntimeError("Cannot reverse this migration. 'Company.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Company.overview'
        raise RuntimeError("Cannot reverse this migration. 'Company.overview' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Company.total_money_raised'
        raise RuntimeError("Cannot reverse this migration. 'Company.total_money_raised' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Company.name'
        raise RuntimeError("Cannot reverse this migration. 'Company.name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'tag.tag'
        raise RuntimeError("Cannot reverse this migration. 'tag.tag' and its values cannot be restored.")


    models = {
        'main.company': {
            'Meta': {'object_name': 'Company'},
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
