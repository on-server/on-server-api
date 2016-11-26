# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FtpUser(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(_('name'), max_length=128, unique=True)
	password = models.CharField(_('login'), max_length=128)
	home = models.CharField(_('home'), max_length=256)
	uid = models.PositiveIntegerField(_('uid'), unique=True)
	gid = models.PositiveIntegerField(_('uid'), unique=True)
	shell = models.CharField(_('shell'), default='/usr/sbin/nologin', max_length=256)
	created_at = models.DateTimeField(_('created at'), blank=True, editable=False, auto_now_add=True)
	updated_at = models.DateTimeField(_('updated at'), blank=True, editable=False, auto_now=True)

	class Meta:
		verbose_name = _('ftp user')
		verbose_name_plural = _('ftp users')
		ordering = ('user', 'name', '-created_at')


class FtpGroup(models.Model):
	name = models.CharField(max_length=254)
	gid = models.PositiveIntegerField()
	members = models.CharField(max_length=254)
	created_at = models.DateTimeField(_('created at'), blank=True, editable=False, auto_now_add=True)
	updated_at = models.DateTimeField(_('updated at'), blank=True, editable=False, auto_now=True)

	class Meta:
		ordering = ('name', 'gid', '-created_at')


class FtpAccess(models.Model):
	name = models.CharField(max_length=254)
	allowed = models.CharField(max_length=254, blank=True, null=True)
	denied = models.CharField(max_length=254, blank=True, null=True)
	options = models.CharField(max_length=254)
	created_at = models.DateTimeField(_('created at'), blank=True, editable=False, auto_now_add=True)
	updated_at = models.DateTimeField(_('updated at'), blank=True, editable=False, auto_now=True)

	class Meta:
		ordering = ('name', '-created_at')
