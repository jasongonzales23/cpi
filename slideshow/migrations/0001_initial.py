# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Slideshow'
        db.create_table('slideshow_slideshow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('slideshow', ['Slideshow'])

        # Adding model 'Slide'
        db.create_table('slideshow_slide', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slideshow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slideshow.Slideshow'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('slide', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('heading_1', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('heading_2', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('headingColor', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('caption', self.gf('django.db.models.fields.TextField')(max_length=255, blank=True)),
            ('captionColor', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('buttonText', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('buttonLink', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('slideshow', ['Slide'])

        # Adding model 'SlideshowPlugin'
        db.create_table('cmsplugin_slideshowplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('slideshow', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['slideshow.Slideshow'])),
        ))
        db.send_create_signal('slideshow', ['SlideshowPlugin'])


    def backwards(self, orm):
        
        # Deleting model 'Slideshow'
        db.delete_table('slideshow_slideshow')

        # Deleting model 'Slide'
        db.delete_table('slideshow_slide')

        # Deleting model 'SlideshowPlugin'
        db.delete_table('cmsplugin_slideshowplugin')


    models = {
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
        },
        'slideshow.slide': {
            'Meta': {'object_name': 'Slide'},
            'buttonLink': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'buttonText': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'captionColor': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'headingColor': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'heading_1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'heading_2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'slide': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slideshow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['slideshow.Slideshow']"}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'slideshow.slideshow': {
            'Meta': {'object_name': 'Slideshow'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'slideshow.slideshowplugin': {
            'Meta': {'object_name': 'SlideshowPlugin', 'db_table': "'cmsplugin_slideshowplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'slideshow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['slideshow.Slideshow']"})
        }
    }

    complete_apps = ['slideshow']
