from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('modified'), auto_now=True)

    class Meta:
        abstract = True


class Capibara(TimeStampedMixin):
    capibara_format = models.CharField(verbose_name=_('capibara_format'), max_length=255)
    capibara_slang = models.CharField(verbose_name=_('capibara_slang'), max_length=255)
    capibara_phrases = models.JSONField(verbose_name=_('capibara_phrases'))

    class Meta:
        db_table = "capibara"
        verbose_name = _('capibara')
        verbose_name_plural = _('capybaras')

    def __str__(self):
        return str(self.id)
