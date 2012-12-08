# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SellerLocation'
        db.create_table(u'seller_sellerlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('raw_json', self.gf('django.db.models.fields.TextField')()),
            ('json', self.gf('django.db.models.fields.TextField')()),
            ('formatted_address', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pnt', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('administrative_area_level_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('administrative_area_level_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('administrative_area_level_3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'seller', ['SellerLocation'])

        # Deleting field 'Seller.pnt'
        db.delete_column(u'seller_seller', 'pnt')

        # Deleting field 'Seller.address'
        db.delete_column(u'seller_seller', 'address')

        # Deleting field 'Seller.lat'
        db.delete_column(u'seller_seller', 'lat')

        # Deleting field 'Seller.lng'
        db.delete_column(u'seller_seller', 'lng')

        # Adding field 'Seller.location'
        db.add_column(u'seller_seller', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seller.SellerLocation'], null=True),
                      keep_default=False)

        # Adding field 'Seller.raw_address'
        db.add_column(u'seller_seller', 'raw_address',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SellerLocation'
        db.delete_table(u'seller_sellerlocation')

        # Adding field 'Seller.pnt'
        db.add_column(u'seller_seller', 'pnt',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Seller.address'
        raise RuntimeError("Cannot reverse this migration. 'Seller.address' and its values cannot be restored.")
        # Adding field 'Seller.lat'
        db.add_column(u'seller_seller', 'lat',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Seller.lng'
        db.add_column(u'seller_seller', 'lng',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Seller.location'
        db.delete_column(u'seller_seller', 'location_id')

        # Deleting field 'Seller.raw_address'
        db.delete_column(u'seller_seller', 'raw_address')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'seller.seller': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Seller'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['seller.SellerCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seller.SellerLocation']", 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'raw_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'seller.sellercategory': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'SellerCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'seller.sellerlocation': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'SellerLocation'},
            'administrative_area_level_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'administrative_area_level_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'administrative_area_level_3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'formatted_address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'pnt': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'raw_json': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['seller']