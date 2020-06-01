from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now as timezone_now


# Base Model.
class BaseModel(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    # Date fields.
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name=_('update at'))

    class Meta:
        abstract = True


# Type
class ItemType(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A type of item with that alias already exists."),
                             }, verbose_name=_('alias'))
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'))
    type = models.CharField(max_length=100, null=False, verbose_name=_('type'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('Item Type')
        verbose_name_plural = _('Item Types')


# Format
class Format(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A format of item with that alias already exists."),
                             }, verbose_name=_('alias'))
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('Format')
        verbose_name_plural = _('Formats')


# State
class State(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A state of item with that alias already exists."),
                             }, verbose_name=_('alias'))
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')


# Level
class Level(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A level of item with that alias already exists."),
                             }, verbose_name=_('alias'))
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('Level')
        verbose_name_plural = _('Levels')


# Language
class Language(models.Model):
    code = models.CharField(max_length=20, null=False, primary_key=True,
                            error_messages={
                                'unique': _("A language of item with that code already exists."),
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


# Section
class Section(BaseModel):
    alias = models.CharField(max_length=100, null=False, verbose_name=_('name'), unique=True)
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'))
    course = models.CharField(max_length=100, verbose_name=_('course'))
    order = models.IntegerField(verbose_name=_('order'))
    is_visible = models.BooleanField(default=False, null=False, verbose_name=_('is visible'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        unique_together = ('course', 'order',)
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')


# Item.
class Item(BaseModel):
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A item with that alias already exists."),
                             }, verbose_name=_('alias'))
    # Config fiedls.
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE, to_field='alias', verbose_name=_('type'))
    format = models.ForeignKey('Format', on_delete=models.CASCADE, null=True,
                               to_field='alias', verbose_name=_('format'))
    state = models.ForeignKey('State', on_delete=models.CASCADE, to_field='alias', verbose_name=_('state'))
    is_visible = models.BooleanField(default=False, null=False, verbose_name=_('is visible'))
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'))
    picture = models.ImageField(null=True, blank=True, verbose_name=_('picture'))
    level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True,
                              blank=True, to_field='alias', verbose_name=_('level'))
    duration = models.IntegerField(null=True, blank=True, verbose_name=_('duration'))
    language = models.ForeignKey('Language', on_delete=models.CASCADE, to_field='code', verbose_name=_('language'))
    tech_tags = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('tech tags'))
    # Date config fields.
    start_at = models.DateTimeField(null=False, default=timezone_now, verbose_name=_('start at'))
    end_at = models.DateTimeField(null=False, default=timezone_now, verbose_name=_('end at'))
    order = models.IntegerField(null=False, verbose_name=_('order'))
    # Relations fields.
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True,
                                blank=True, to_field='alias', verbose_name=_('section'))

    # Class Meta.
    class Meta:
        unique_together = ('section', 'order',)
        verbose_name = _('Item')
        verbose_name_plural = _('Items')

