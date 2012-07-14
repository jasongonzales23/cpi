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

SIZE_CHOICES =(
    ('small','small'),
    ('medium', 'medium'),
    ('large', 'large'),)

WEIGHT_CHOICES = (
    ('normal','normal'),
    ('bold', 'bold'),)

class BannerPlugin(CMSPlugin):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/bannerImages")
    textColor = models.CharField(max_length=20, choices=COLOR_CHOICES)
    textSize = models.CharField(max_length=30, choices=SIZE_CHOICES, default="large")
    textWeight = models.CharField(max_length=30, choices=WEIGHT_CHOICES, default="bold")
    
    def __unicode__(self):
        return self.name
