# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Contact.last_name_label'
        db.add_column('cmsplugin_contact', 'last_name_label', self.gf('django.db.models.fields.CharField')(default=u'Last Name', max_length=100), keep_default=False)

        # Adding field 'Contact.company_label'
        db.add_column('cmsplugin_contact', 'company_label', self.gf('django.db.models.fields.CharField')(default=u'Company', max_length=100), keep_default=False)

        # Adding field 'Contact.city_label'
        db.add_column('cmsplugin_contact', 'city_label', self.gf('django.db.models.fields.CharField')(default=u'City', max_length=100), keep_default=False)

        # Adding field 'Contact.state_label'
        db.add_column('cmsplugin_contact', 'state_label', self.gf('django.db.models.fields.CharField')(default=u'State', max_length=100), keep_default=False)

        # Adding field 'Contact.postal_code_label'
        db.add_column('cmsplugin_contact', 'postal_code_label', self.gf('django.db.models.fields.CharField')(default=u'Postal code', max_length=100), keep_default=False)

        # Adding field 'Contact.country_label'
        db.add_column('cmsplugin_contact', 'country_label', self.gf('django.db.models.fields.CharField')(default=u'Country', max_length=100), keep_default=False)

        # Adding field 'Contact.phone_label'
        db.add_column('cmsplugin_contact', 'phone_label', self.gf('django.db.models.fields.CharField')(default=u'Phone', max_length=100), keep_default=False)

        # Adding field 'Contact.company_site_label'
        db.add_column('cmsplugin_contact', 'company_site_label', self.gf('django.db.models.fields.CharField')(default=u'Company site', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Contact.last_name_label'
        db.delete_column('cmsplugin_contact', 'last_name_label')

        # Deleting field 'Contact.company_label'
        db.delete_column('cmsplugin_contact', 'company_label')

        # Deleting field 'Contact.city_label'
        db.delete_column('cmsplugin_contact', 'city_label')

        # Deleting field 'Contact.state_label'
        db.delete_column('cmsplugin_contact', 'state_label')

        # Deleting field 'Contact.postal_code_label'
        db.delete_column('cmsplugin_contact', 'postal_code_label')

        # Deleting field 'Contact.country_label'
        db.delete_column('cmsplugin_contact', 'country_label')

        # Deleting field 'Contact.phone_label'
        db.delete_column('cmsplugin_contact', 'phone_label')

        # Deleting field 'Contact.company_site_label'
        db.delete_column('cmsplugin_contact', 'company_site_label')


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
        'cmsplugin_contact.contact': {
            'Meta': {'object_name': 'Contact', 'db_table': "'cmsplugin_contact'"},
            'akismet_api_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city_label': ('django.db.models.fields.CharField', [], {'default': "u'City'", 'max_length': '100'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'company_label': ('django.db.models.fields.CharField', [], {'default': "u'Company'", 'max_length': '100'}),
            'company_site_label': ('django.db.models.fields.CharField', [], {'default': "u'Company site'", 'max_length': '100'}),
            'content_label': ('django.db.models.fields.CharField', [], {'default': "u'Message'", 'max_length': '100'}),
            'country_label': ('django.db.models.fields.CharField', [], {'default': "u'Country'", 'max_length': '100'}),
            'email_label': ('django.db.models.fields.CharField', [], {'default': "u'Your email address'", 'max_length': '100'}),
            'first_name_label': ('django.db.models.fields.CharField', [], {'default': "u'First Name'", 'max_length': '100'}),
            'last_name_label': ('django.db.models.fields.CharField', [], {'default': "u'Last Name'", 'max_length': '100'}),
            'phone_label': ('django.db.models.fields.CharField', [], {'default': "u'Phone'", 'max_length': '100'}),
            'postal_code_label': ('django.db.models.fields.CharField', [], {'default': "u'Postal code'", 'max_length': '100'}),
            'recaptcha_private_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'recaptcha_public_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'recaptcha_theme': ('django.db.models.fields.CharField', [], {'default': "'clean'", 'max_length': '20'}),
            'site_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'spam_protection_method': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'state_label': ('django.db.models.fields.CharField', [], {'default': "u'State'", 'max_length': '100'}),
            'subject_label': ('django.db.models.fields.CharField', [], {'default': "u'Subject'", 'max_length': '200'}),
            'submit': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '30'}),
            'thanks': ('django.db.models.fields.TextField', [], {'default': "u'Thank you for your message.'", 'max_length': '200'})
        }
    }

    complete_apps = ['cmsplugin_contact']
