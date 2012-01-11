from django.db import models
from django.forms import ModelForm
from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import CheckboxInput


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    url = models.CharField(max_length=255)
    newsletter = models.BooleanField()
    comments = models.TextField(max_length=255)
    
    def __unicode__(self):
        return self.first_name
    
    #TODO finish this
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'company', )
    