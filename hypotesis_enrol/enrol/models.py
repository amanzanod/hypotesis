from django.db import models
from django.utils.translation import gettext_lazy as _


# State
class State(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    alias = models.CharField(max_length=20, null=False, primary_key=True,
                             error_messages={
                                 'unique': _("A state of enrol with that alias already exists."),
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


# Enrol Context
class EnrolContext(models.Model):
    user = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    context = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    role = models.CharField(max_length=100, null=False, verbose_name=_('name'))
    state = models.ForeignKey('State', on_delete=models.CASCADE, to_field='alias', verbose_name=_('state'))
    state_at = models.DateTimeField(null=True, blank=True, verbose_name=_('state at'))
    # Date fields.
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name=_('update at'))

    # Format str.
    def __str__(self):
        return self.user + ' - ' + self.context + '(' + self.role + ')'
