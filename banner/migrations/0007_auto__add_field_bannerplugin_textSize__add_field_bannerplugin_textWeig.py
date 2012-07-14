# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'BannerPlugin.textSize'
        db.add_column('cmsplugin_bannerplugin', 'textSize', self.gf('django.db.models.fields.CharField')(default='large', max_length=30), keep_default=False)

        # Adding field 'BannerPlugin.textWeight'
        db.add_column('cmsplugin_bannerplugin', 'textWeight', self.gf('django.db.models.fields.CharField')(default='bold', max_length=30), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'BannerPlugin.textSize'
        db.delete_column('cmsplugin_bannerplugin', 'textSize')

        # Deleting field 'BannerPlugin.textWeight'
        db.delete_column('cmsplugin_bannerplugin', 'textWeight')


    models = {
        'banner.bannerplugin': {
            'Meta': {'object_name': 'BannerPlugin', 'db_table': "'cmsplugin_bannerplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'textColor': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'textSize': ('django.db.models.fields.CharField', [], {'default': "'large'", 'max_length': '30'}),
            'textWeight': ('django.db.models.fields.CharField', [], {'default': "'bold'", 'max_length': '30'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['banner']
