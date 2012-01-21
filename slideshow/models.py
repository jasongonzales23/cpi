from django.db import models
from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

COLOR_CHOICES = (('teal','teal'), ('dk-grey','dark grey'), ('lt-grey','light grey'), ('white','white'), ('black','black'),)

class Slideshow(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('slideshow_view', args=[self.pk])
    class Meta:
        verbose_name_plural = 'slideshow'
    
class Slide(models.Model):
    slideshow = models.ForeignKey(Slideshow)
    order = models.IntegerField()
    slide = models.ImageField(upload_to="uploads/slideshowImages/")
    thumbnail = models.ImageField(upload_to="uploads/slideshowImages")
    heading_1 = models.CharField(max_length=50, blank=True)
    heading_2 = models.CharField(max_length=50, blank=True)
    headingColor = models.CharField(max_length=20, choices=COLOR_CHOICES)
    caption = models.TextField(max_length=255, blank=True)
    captionColor = models.CharField(max_length=20, choices=COLOR_CHOICES)
    buttonText = models.CharField(max_length=50, blank=True)
    buttonLink = models.CharField(max_length=50, blank=True)
    
    class Meta:
        ordering = ["order"]
    
    def __unicode__(self):
        return str(self.order)
#stuff you need to make it a plugin
from cms.models import CMSPlugin

class SlideshowPlugin(CMSPlugin):
    slideshow = models.ForeignKey('slideshow.Slideshow', related_name='plugins')
    
    def __unicode__(self):
        return self.slideshow.name

