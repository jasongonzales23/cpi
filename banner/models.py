from django.db import models
    
#stuff you need to make it a plugin
from cms.models import CMSPlugin

COLOR_CHOICES = (('teal','teal'),
    ('dk-grey','dark grey'),
    ('lt-grey','light grey'),
    ('white','white'),
    ('black','black'),
    ('green','green'),
    ('red','red'),)

class BannerPlugin(CMSPlugin):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/bannerImages")
    textColor = models.CharField(max_length=20, choices=COLOR_CHOICES)
    
    def __unicode__(self):
        return self.name