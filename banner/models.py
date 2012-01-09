from django.db import models
    
#stuff you need to make it a plugin
from cms.models import CMSPlugin

class BannerPlugin(CMSPlugin):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploads/bannerImages")
    #banner = models.ForeignKey('banner.Banner', related_name='plugins')
    
    def __unicode__(self):
        return self.name