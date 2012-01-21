from slideshow.models import Slideshow, Slide
from django.contrib import admin
#from cms.admin.placeholderadmin import PlaceholderAdmin

class SlideInline(admin.StackedInline):
    model = Slide
    
class SlideshowAdmin(admin.ModelAdmin):
    inlines = [SlideInline,]

    
admin.site.register(Slideshow, SlideshowAdmin)