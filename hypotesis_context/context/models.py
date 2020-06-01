from django.db import models
from django.utils.timezone import now as timezone_now
from django.utils.translation import gettext_lazy as _


# Base Model.
class BaseModel(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    # Date fields.
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name=_('update at'))
    visible_at = models.DateTimeField(null=True, blank=True, verbose_name=_('visible at'))
    state_at = models.DateTimeField(null=True, blank=True, verbose_name=_('state at'))

    # Meta.
    class Meta:
        abstract = True

    # Format str.
    def __str__(self):
        return self.name


# Type
class ContextType(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A type of context with that alias already exists."),
                             }, verbose_name=_('alias'))
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'))

    # Format str.
    def __str__(self):
        return self.name

    # Class Meta.
    class Meta:
        verbose_name = _('Context Type')
        verbose_name_plural = _('Context Types')


# Format
class Format(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A format of context with that alias already exists."),
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
                                 'unique': _("A state of context with that alias already exists."),
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
                                 'unique': _("A level of context with that alias already exists."),
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
                                'unique': _("A language of context with that code already exists."),
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


# Context.
class Context(BaseModel):
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A context of this type with that alias already exists."),
                             }, verbose_name=_('alias'))
    # Config fiedls.
    type = models.ForeignKey(ContextType, on_delete=models.CASCADE, to_field='alias', verbose_name=_('type'))
    format = models.ForeignKey('Format', on_delete=models.CASCADE, null=True,
                               to_field='alias', verbose_name=_('format'))
    state = models.ForeignKey('State', on_delete=models.CASCADE, to_field='alias', verbose_name=_('state'))
    is_visible = models.BooleanField(default=False, null=False, verbose_name=_('is visible'))
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('description'))
    picture = models.ImageField(null=True, blank=True, verbose_name=_('picture'))
    syllabus = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('syllabus'))
    requeriments = models.TextField(max_length=500, null=True, blank=True, verbose_name=_('requeriments'))
    level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True,
                              blank=True, to_field='alias', verbose_name=_('level'))
    duration = models.IntegerField(null=True, blank=True, verbose_name=_('duration'))
    language = models.ForeignKey('Language', on_delete=models.CASCADE, to_field='code', verbose_name=_('language'))
    tech_tags = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('tech tags'))
    # Date config fields.
    start_at = models.DateTimeField(null=False, default=timezone_now, verbose_name=_('start at'))
    end_at = models.DateTimeField(null=False, default=timezone_now, verbose_name=_('end at'))
    # Relations fields.
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                               blank=True, to_field='alias', verbose_name=_('parent'))
    teacher_main = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('teacher main'))
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, to_field='alias',
                                 verbose_name=_('category'))

    # Class Meta.
    class Meta:
        verbose_name = _('Context')
        verbose_name_plural = _('Contexts')


# Category.
class Category(BaseModel):
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A category with that alias already exists."),
                             }, verbose_name=_('alias'))
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name=_('description'))
    # State fields.
    state = models.ForeignKey('State', on_delete=models.CASCADE, to_field='alias', verbose_name=_('state'))
    is_visible = models.BooleanField(default=False, null=False, verbose_name=_('is visible'))
    # Relations fields.
    context_type = models.ForeignKey('ContextType', on_delete=models.CASCADE, to_field='alias', verbose_name=_('type'))
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                               blank=True, to_field='alias', verbose_name=_('parent'))
