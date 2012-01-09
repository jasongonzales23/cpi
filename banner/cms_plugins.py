from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from banner.models import BannerPlugin as BannerPluginModel
from cms.models.pluginmodel import CMSPlugin 
from django.utils.translation import ugettext_lazy as _

class CMSBannerPlugin(CMSPluginBase):
    model = BannerPluginModel
    name = _("Banner Plugin")
    render_template = "banner_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'bannerplugin':instance.bannerplugin,
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSBannerPlugin)