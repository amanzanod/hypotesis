from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now as timezone_now


# Base Model.
class BaseModel(models.Model):
    # Date fields.
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        abstract = True


# Context.
class Context(BaseModel):
    name = models.CharField(max_length=50, null=False)
    alias = models.CharField(max_length=20, null=False, unique=True,
                             error_messages={
                                 'unique': _("A context with that alias already exists."),
                             })

    # Format str.
    def __str__(self):
        return self.alias


# Role.
class Role(BaseModel):
    name = models.CharField(max_length=100, null=False)
    state = models.SmallIntegerField(default=0, null=False)
    is_visible = models.BooleanField(default=False, null=False)
    icon = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    alias = models.CharField(max_length=20, null=False, unique=True,
                             error_messages={
                                 'unique': _("A role with that alias already exists."),
                             })
    # Relations fields.
    permissions = models.ManyToManyField('Permission', through='PermissionRole', blank=True)
    # Date fields.
    visible_at = models.DateTimeField(null=True, blank=True)
    state_at = models.DateTimeField(null=True, blank=True)

    # Format str.
    def __str__(self):
        return self.name


# Permission.
class Permission(BaseModel):
    alias = models.CharField(max_length=20, null=False, unique=True,
                             error_messages={
                                 'unique': _("A permission with that alias already exists."),
                             })
    state = models.SmallIntegerField(default=0, null=False)
    is_visible = models.BooleanField(default=False, null=False)
    description = models.TextField(max_length=200, null=True, blank=True)
    # Relations fields.
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    roles = models.ManyToManyField('Role', through='PermissionRole', blank=True)
    # Date fields.
    visible_at = models.DateTimeField(null=True, blank=True)
    state_at = models.DateTimeField(null=True, blank=True)

    # Format str.
    def __str__(self):
        return self.alias


# PermissionRole.
class PermissionRole(BaseModel):
    # Relations fields.
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=False, null=False)
    # Date fields.
    active_at = models.DateTimeField(null=True, blank=True)

    # Meta.
    class Meta:
        unique_together = ('role', 'permission',)

    # Format str.
    def __str__(self):
        return str(self.role) + '-' + str(self.permission)


# User.
class User(BaseModel):
    # User fields.
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    # States fields.
    state = models.SmallIntegerField(default=0, null=False)
    is_visible = models.BooleanField(default=False, null=False)
    # Title fields.
    name = models.CharField(max_length=100, null=False)
    surname1 = models.CharField(max_length=100, null=False)
    surname2 = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    # Contact fields.
    email = models.EmailField(null=False)
    city = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    # Config fields.
    language = models.CharField(max_length=20, null=True, blank=True)
    # Description fields.
    about_me = models.TextField(max_length=500, null=True, blank=True)
    # Date fields.
    visible_at = models.DateTimeField(null=True, blank=True)
    state_at = models.DateTimeField(null=True, blank=True)
    # Relations fields.
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    # Format str.
    def __str__(self):
        str_format = ''
        str_format = str_format + ' ' + str(self.name) if self.name else str_format
        str_format = str_format + ' ' + str(self.surname1) if self.surname1 else str_format
        str_format = str_format + ' ' + str(self.surname2) if self.surname2 else str_format
        return str_format
