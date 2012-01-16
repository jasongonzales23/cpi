from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

# Feel free to extend this class instead of Contact.
class BaseContact(CMSPlugin):
    SPAM_PROTECTION_CHOICES = (
        (0, 'Honeypot'),
        (1, 'Akismet'),
        (2, 'ReCAPTCHA'),
    )
    
    THEME_CHOICES = (
        ('clean', 'Clean'),
        ('red', 'Red'),
        ('white', 'White'),
        ('blackglass', 'Black Glass'),
        ('custom', 'Custom'),
    )
    site_email = models.EmailField(_('Email recipient'))
    first_name_label = models.CharField(_('First name label'),
                                        default=_('First Name'),
                                        max_length=100)
    last_name_label = models.CharField(_('Last name label'),
                                        default=_('Last Name'),
                                        max_length=100)
    company_label = models.CharField(_('First name label'),
                                        default=_('Company'),
                                        max_length=100)
    city_label = models.CharField(_('City label'),
                                        default=_('City'),
                                        max_length=100)
    state_label = models.CharField(_('State label'),
                                        default=_('State'),
                                        max_length=100)
    postal_code_label = models.CharField(_('Postal code label'),
                                        default=_('Postal code'),
                                        max_length=100)
    country_label = models.CharField(_('Country label'),
                                        default=_('Country'),
                                        max_length=100)
    phone_label = models.CharField(_('Phone label'),
                                        default=_('Phone'),
                                        max_length=100)
    company_site_label = models.CharField(_('Company site label'),
                                        default=_('Company site'),
                                        max_length=100)
    email_label = models.CharField(_('Email sender label'),
                                   default=_('Your email address'),
                                   max_length=100)
    subject_label = models.CharField(_('Subject label'),
                                     default=_('Subject'), max_length=200)
    content_label = models.CharField(_('Message content label'),
                                     default=_('Message'), max_length=100)
    thanks = models.TextField(
        verbose_name=_("Thanks message"),
        help_text=_('Message displayed on successful submit'),
        default=_('Thank you for your message.'), max_length=200)
    submit = models.CharField(_('Submit button value'),
                              default=_('Submit'), max_length=30)
    
    spam_protection_method = models.SmallIntegerField(
        verbose_name=_('Spam protection method'),
        choices=SPAM_PROTECTION_CHOICES, default=0)
    
    akismet_api_key = models.CharField(max_length=255, blank=True)
    
    recaptcha_public_key = models.CharField(max_length=255, blank=True)
    recaptcha_private_key = models.CharField(max_length=255, blank=True)
    recaptcha_theme = models.CharField(max_length=20,
                                       choices=THEME_CHOICES,
                                       default='clean',
                                       verbose_name=_('ReCAPTCHA theme'))

    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.site_email

class Contact(BaseContact):
    pass
