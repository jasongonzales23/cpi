from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from slideshow.models import SlideshowPlugin as SlideshowPluginModel
from django.utils.translation import ugettext as _

class SlideshowPlugin(CMSPluginBase):
    model = SlideshowPluginModel
    name = _("Slideshow")
    render_template = "slideshow.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'slideshow':instance.slideshow,
            'object':instance,
            'placeholder':placeholder
        })
        return context
    
plugin_pool.register_plugin(SlideshowPlugin)