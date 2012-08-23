# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Price'
        db.create_table('currencies_price', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Product'])),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['currencies.Currency'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=4)),
        ))
        db.send_create_signal('currencies', ['Price'])


    def backwards(self, orm):
        # Deleting model 'Price'
        db.delete_table('currencies_price')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        'currencies.price': {
            'Meta': {'object_name': 'Price'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['currencies.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']"})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'})
        }
    }

    complete_apps = ['currencies']