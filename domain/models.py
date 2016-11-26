# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Domain(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'))
    name = models.CharField(_('domain'), max_length=254)
    alias = models.CharField(_('alias'), max_length=254)
    created_at = models.DateTimeField(_('created at'), blank=True, editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), blank=True, editable=False, auto_now=True)

    class Meta:
        verbose_name = _('domain')
        verbose_name_plural = _('domains')
        ordering = ('name', '-created_at')
