# -*- coding: utf-8 -*-
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email'), unique=True)
    created_at = models.DateTimeField(_('created at'), blank=True, editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), blank=True, editable=False, auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('email', '-date_joined',)

    def get_full_name(self):
        name = "{} {}".format(self.first_name, self.last_name).strip()
        return name if name else self.email

    def get_short_name(self):
        return self.username
