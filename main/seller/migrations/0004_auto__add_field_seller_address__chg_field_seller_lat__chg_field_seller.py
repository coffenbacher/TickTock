# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Seller.address'
        db.add_column('seller_seller', 'address',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'Seller.lat'
        db.alter_column('seller_seller', 'lat', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Seller.lng'
        db.alter_column('seller_seller', 'lng', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Seller.address'
        db.delete_column('seller_seller', 'address')


        # User chose to not deal with backwards NULL issues for 'Seller.lat'
        raise RuntimeError("Cannot reverse this migration. 'Seller.lat' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Seller.lng'
        raise RuntimeError("Cannot reverse this migration. 'Seller.lng' and its values cannot be restored.")

    models = {
        'seller.seller': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Seller'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['seller.SellerCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'seller.sellercategory': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'SellerCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['seller']