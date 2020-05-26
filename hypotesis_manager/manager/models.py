from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Base Model.
class BaseModel(models.Model):
    # Date fields.
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name=_('update at'))

    class Meta:
        abstract = True


# Context.
class Context(BaseModel):
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A context with that alias already exists."),
                             }, verbose_name=_('alias'))
    name = models.CharField(max_length=50, null=False, verbose_name=_('name'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('Context')
        verbose_name_plural = _('Contexts')


# State
class State(models.Model):
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A state with that alias already exists."),
                             }, verbose_name=_('alias'))
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')


# Country
class Country(models.Model):
    code = models.CharField(max_length=20, null=False, primary_key=True,
                            error_messages={
                                'unique': _("A country with that code already exists."),
                            }, verbose_name=_('code'))
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    original_name = models.CharField(max_length=100, null=True, verbose_name=_('original name'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


# Province
class Province(models.Model):
    code = models.CharField(max_length=20, null=False, primary_key=True,
                            error_messages={
                                'unique': _("A province with that code already exists."),
                            }, verbose_name=_('code'))
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    original_name = models.CharField(max_length=100, null=True, verbose_name=_('original_name'))

    country = models.ForeignKey(Country, on_delete=models.CASCADE, to_field='code', verbose_name=_('country'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')


# Language
class Language(models.Model):
    code = models.CharField(max_length=20, null=False, primary_key=True,
                            error_messages={
                                'unique': _("A language of with that code already exists."),
                            }, verbose_name=_('code'))
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')


# Role.
class Role(BaseModel):
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A role with that alias already exists."),
                             }, verbose_name=_('alias'))
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    state = models.ForeignKey('State', on_delete=models.CASCADE, to_field='alias', verbose_name=_('state'))
    is_visible = models.BooleanField(default=False, null=False, verbose_name=_('is_visible'))
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('icon'))
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name=_('description'))
    # Relations fields.
    permissions = models.ManyToManyField('Permission', through='PermissionRole', blank=True,
                                         verbose_name=_('permission'))
    # Date fields.
    visible_at = models.DateTimeField(null=True, blank=True, verbose_name=_('visible at'))
    state_at = models.DateTimeField(null=True, blank=True, verbose_name=_('state at'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')


# Permission.
class Permission(BaseModel):
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A permission with that alias already exists."),
                             }, verbose_name=_('alias'))
    state = models.ForeignKey('State', on_delete=models.CASCADE, to_field='alias', verbose_name=_('state'))
    is_visible = models.BooleanField(default=False, null=False, verbose_name=_('is visible'))
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name=_('description'))
    # Relations fields.
    context = models.ForeignKey(Context, on_delete=models.CASCADE, to_field='alias', verbose_name=_('context'))
    roles = models.ManyToManyField('Role', through='PermissionRole', blank=True, verbose_name=_('roles'))
    # Date fields.
    visible_at = models.DateTimeField(null=True, blank=True, verbose_name=_('visible_at'))
    state_at = models.DateTimeField(null=True, blank=True, verbose_name=_('state_at'))

    # Format str.
    def __str__(self):
        return self.alias

    # Class Meta.
    class Meta:
        verbose_name = _('Permission')
        verbose_name_plural = _('Permissions')


# PermissionRole.
class PermissionRole(BaseModel):
    # Relations fields.
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name=_('role'))
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, verbose_name=_('permission'))

    is_active = models.BooleanField(default=False, null=False, verbose_name=_('is active'))
    # Date fields.
    active_at = models.DateTimeField(null=True, blank=True, verbose_name=_('active at'))

    # Meta.
    class Meta:
        unique_together = ('role', 'permission',)
        verbose_name = _('Role permission')
        verbose_name_plural = _('Role permissions')

    # Format str.
    def __str__(self):
        return str(self.role) + '-' + str(self.permission)


# User Manager.
class UserManager(BaseModel):
    # User fields.
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=150,
        primary_key=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        }, verbose_name=_('username'),
    )
    password = models.CharField(max_length=100, verbose_name=_('password'))
    token = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('token'))
    picture = models.ImageField(null=True, blank=True, upload_to='profile', verbose_name=_('picture'))
    # States fields.
    state = models.ForeignKey('State', on_delete=models.CASCADE, to_field='alias', verbose_name=_('state'))
    is_visible = models.BooleanField(default=False, null=False, verbose_name=_('is visible'))
    # Title fields.
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    surname1 = models.CharField(max_length=100, null=False, verbose_name=_('first surname'))
    surname2 = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('second surname'))
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('title'))
    # Contact fields.
    email = models.EmailField(null=False, verbose_name=_('e-mail'))
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('city'))
    province = models.ForeignKey(Province, null=True, on_delete=models.SET_NULL,
                                 to_field='code', verbose_name=_('province'))
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL,
                                to_field='code', verbose_name=_('country'))
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('address'))
    postal_code = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('postal code'))
    # Config fields.
    language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL,
                                 to_field='code', verbose_name=_('language'))
    # Description fields.
    about_me = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('about_me'))
    # Date fields.
    visible_at = models.DateTimeField(null=True, blank=True, verbose_name=_('visible at'))
    state_at = models.DateTimeField(null=True, blank=True, verbose_name=_('state at'))
    # Relations fields.
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True,
                             to_field='alias', verbose_name=_('role'))

    # Format str.
    def __str__(self):
        str_format = ''
        str_format = str_format + ' ' + str(self.name) if self.name else str_format
        str_format = str_format + ' ' + str(self.surname1) if self.surname1 else str_format
        str_format = str_format + ' ' + str(self.surname2) if self.surname2 else str_format
        return str_format

    # Class Meta.
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
