# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Currency'
        db.create_table('currencies_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(default='1', max_digits=12, decimal_places=4)),
            ('spread', self.gf('django.db.models.fields.DecimalField')(default='2.5', max_digits=12, decimal_places=4)),
            ('before', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('after', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('decimal_places', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('separator', self.gf('django.db.models.fields.CharField')(default=u',', max_length=1)),
            ('decimal_point', self.gf('django.db.models.fields.CharField')(default=u'.', max_length=1)),
        ))
        db.send_create_signal('currencies', ['Currency'])

        # Adding model 'Country'
        db.create_table('currencies_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['currencies.Currency'])),
        ))
        db.send_create_signal('currencies', ['Country'])


    def backwards(self, orm):
        
        # Deleting model 'Currency'
        db.delete_table('currencies_currency')

        # Deleting model 'Country'
        db.delete_table('currencies_country')


    models = {
        'currencies.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['currencies.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'currencies.currency': {
            'Meta': {'object_name': 'Currency'},
            'after': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'before': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'decimal_places': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'decimal_point': ('django.db.models.fields.CharField', [], {'default': "u'.'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'default': "'1'", 'max_digits': '12', 'decimal_places': '4'}),
            'separator': ('django.db.models.fields.CharField', [], {'default': "u','", 'max_length': '1'}),
            'spread': ('django.db.models.fields.DecimalField', [], {'default': "'2.5'", 'max_digits': '12', 'decimal_places': '4'})
        }
    }

    complete_apps = ['currencies']
