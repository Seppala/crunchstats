# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Company'
        db.create_table('main_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('permalink', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('number_of_employees', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('founded_year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('founded_month', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('deadpooled_year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('deadpooled_month', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('deadpooled_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('overview', self.gf('django.db.models.fields.TextField')()),
            ('total_money_raised', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('main', ['Company'])

        # Adding M2M table for field tag_list on 'Company'
        db.create_table('main_company_tag_list', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm['main.company'], null=False)),
            ('tag', models.ForeignKey(orm['main.tag'], null=False))
        ))
        db.create_unique('main_company_tag_list', ['company_id', 'tag_id'])

        # Adding M2M table for field funding_rounds on 'Company'
        db.create_table('main_company_funding_rounds', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm['main.company'], null=False)),
            ('funding_rounds', models.ForeignKey(orm['main.funding_rounds'], null=False))
        ))
        db.create_unique('main_company_funding_rounds', ['company_id', 'funding_rounds_id'])

        # Adding M2M table for field ipo on 'Company'
        db.create_table('main_company_ipo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm['main.company'], null=False)),
            ('ipo', models.ForeignKey(orm['main.ipo'], null=False))
        ))
        db.create_unique('main_company_ipo', ['company_id', 'ipo_id'])

        # Adding model 'tag'
        db.create_table('main_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('main', ['tag'])

        # Adding model 'ipo'
        db.create_table('main_ipo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('valuation_amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('valuation_currency_code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pub_year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pub_month', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('pub_day', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('stock_symbol', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('main', ['ipo'])

        # Adding model 'funding_rounds'
        db.create_table('main_funding_rounds', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('round_code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('raised_amount', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('raised_currency_code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('funded_year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('funded_month', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('funded_day', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('main', ['funding_rounds'])

        # Adding M2M table for field investments on 'funding_rounds'
        db.create_table('main_funding_rounds_investments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('funding_rounds', models.ForeignKey(orm['main.funding_rounds'], null=False)),
            ('investments', models.ForeignKey(orm['main.investments'], null=False))
        ))
        db.create_unique('main_funding_rounds_investments', ['funding_rounds_id', 'investments_id'])

        # Adding model 'investments'
        db.create_table('main_investments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fool', self.gf('django.db.models.fields.CharField')(default='jappa', max_length=20)),
        ))
        db.send_create_signal('main', ['investments'])

        # Adding M2M table for field company on 'investments'
        db.create_table('main_investments_company', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('investments', models.ForeignKey(orm['main.investments'], null=False)),
            ('company', models.ForeignKey(orm['main.company'], null=False))
        ))
        db.create_unique('main_investments_company', ['investments_id', 'company_id'])

        # Adding M2M table for field financial_org on 'investments'
        db.create_table('main_investments_financial_org', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('investments', models.ForeignKey(orm['main.investments'], null=False)),
            ('financial_org', models.ForeignKey(orm['main.financial_org'], null=False))
        ))
        db.create_unique('main_investments_financial_org', ['investments_id', 'financial_org_id'])

        # Adding M2M table for field person on 'investments'
        db.create_table('main_investments_person', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('investments', models.ForeignKey(orm['main.investments'], null=False)),
            ('person', models.ForeignKey(orm['main.person'], null=False))
        ))
        db.create_unique('main_investments_person', ['investments_id', 'person_id'])

        # Adding model 'Investment_name'
        db.create_table('main_investment_name', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('financial_org', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('person', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('main', ['Investment_name'])

        # Adding model 'financial_org'
        db.create_table('main_financial_org', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('permalink', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('main', ['financial_org'])

        # Adding model 'person'
        db.create_table('main_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('permalink', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('main', ['person'])


    def backwards(self, orm):
        
        # Deleting model 'Company'
        db.delete_table('main_company')

        # Removing M2M table for field tag_list on 'Company'
        db.delete_table('main_company_tag_list')

        # Removing M2M table for field funding_rounds on 'Company'
        db.delete_table('main_company_funding_rounds')

        # Removing M2M table for field ipo on 'Company'
        db.delete_table('main_company_ipo')

        # Deleting model 'tag'
        db.delete_table('main_tag')

        # Deleting model 'ipo'
        db.delete_table('main_ipo')

        # Deleting model 'funding_rounds'
        db.delete_table('main_funding_rounds')

        # Removing M2M table for field investments on 'funding_rounds'
        db.delete_table('main_funding_rounds_investments')

        # Deleting model 'investments'
        db.delete_table('main_investments')

        # Removing M2M table for field company on 'investments'
        db.delete_table('main_investments_company')

        # Removing M2M table for field financial_org on 'investments'
        db.delete_table('main_investments_financial_org')

        # Removing M2M table for field person on 'investments'
        db.delete_table('main_investments_person')

        # Deleting model 'Investment_name'
        db.delete_table('main_investment_name')

        # Deleting model 'financial_org'
        db.delete_table('main_financial_org')

        # Deleting model 'person'
        db.delete_table('main_person')


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
        'main.investment_name': {
            'Meta': {'object_name': 'Investment_name'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'financial_org': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'main.investments': {
            'Meta': {'object_name': 'investments'},
            'company': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Investments_company'", 'null': 'True', 'to': "orm['main.Company']"}),
            'financial_org': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Investments_financial_org'", 'null': 'True', 'to': "orm['main.financial_org']"}),
            'fool': ('django.db.models.fields.CharField', [], {'default': "'jappa'", 'max_length': '20'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.tag': {
            'Meta': {'object_name': 'tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']
