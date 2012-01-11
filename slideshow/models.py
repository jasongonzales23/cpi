from django.db import models

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
    slide = models.ImageField(upload_to="uploads/slideshowImages/")
    thumbnail = models.ImageField(upload_to="uploads/slideshowImages")
    description = models.CharField(max_length=60)
    buttonText = models.CharField(max_length=255)
    
    
#stuff you need to make it a plugin
from cms.models import CMSPlugin

class SlideshowPlugin(CMSPlugin):
    slideshow = models.ForeignKey('slideshow.Slideshow', related_name='plugins')
    
    def __unicode__(self):
        return self.slideshow.name

