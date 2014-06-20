# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Document.status'
        db.add_column(u'projects_document', 'status',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Document.status'
        db.delete_column(u'projects_document', 'status')


    models = {
        u'home.customers': {
            'Meta': {'object_name': 'Customers'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'new_field': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100'})
        },
        u'projects.document': {
            'Meta': {'object_name': 'Document'},
            'docfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        },
        u'projects.newproject': {
            'Meta': {'object_name': 'NewProject'},
            'customer_id': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['home.Customers']", 'unique': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'disease': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'ftp_file': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'optional': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'tissue': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'upload_file': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['projects']