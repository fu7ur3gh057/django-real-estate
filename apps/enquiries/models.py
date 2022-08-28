from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel


class Enquiry(TimeStampedUUIDModel):
    name = models.CharField(_('Your Name'), max_length=100)
    phone_number = PhoneNumberField(_("Phone Number"), max_length=30, default="+25073243101")
    email = models.EmailField(_("Email"))
    subject = models.CharField(_("Subject"), max_length=100)
    message = models.TextField(_("Message"))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Enquiries"
