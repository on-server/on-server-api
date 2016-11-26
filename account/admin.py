# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Permission
from django.utils.translation import ugettext_lazy as _

from .models import User


class MyUserChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model = User


class MyUserAdmin(UserAdmin):
	form = MyUserChangeForm
	readonly_fields = ('date_joined', 'updated_at', 'created_at', 'last_login')
	fieldsets = (
		(None, {'fields': ('email', 'username', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name',)}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('date_joined', 'last_login', 'updated_at', 'created_at')}),
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'username', 'password1', 'password2'),
		}),
	)

	list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'created_at', 'updated_at', 'last_login')

	search_fields = ('email', 'username', 'first_name', 'last_name', 'email')
	ordering = ('email', 'username')


admin.site.register(User, MyUserAdmin)
admin.site.register(Permission)
