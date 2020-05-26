from django.db import models
from django.utils.timezone import now as timezone_now
from django.utils.translation import gettext_lazy as _


# Base Model.
class BaseModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    # Date fields.
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    visible_at = models.DateTimeField(null=True, blank=True)
    state_at = models.DateTimeField(null=True, blank=True)

    # Meta.
    class Meta:
        abstract = True

    # Format str.
    def __str__(self):
        return self.name


# Type
class ContextType(models.Model):
    name = models.CharField(max_length=100, null=False)
    alias = models.CharField(max_length=20, null=False, unique=True,
                             error_messages={
                                 'unique': _("A type of context with that alias already exists."),
                             })
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True)

    # Format str.
    def __str__(self):
        return self.name


# Format
class Format(models.Model):
    name = models.CharField(max_length=100, null=False)
    alias = models.CharField(max_length=20, null=False, unique=True,
                             error_messages={
                                 'unique': _("A format of context with that alias already exists."),
                             })
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True)

    # Format str.
    def __str__(self):
        return self.name


# State
class State(models.Model):
    name = models.CharField(max_length=100, null=False)
    alias = models.CharField(max_length=20, null=False, unique=True,
                             error_messages={
                                 'unique': _("A state of context with that alias already exists."),
                             })
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True)

    # Format str.
    def __str__(self):
        return self.name


# Level
class Level(models.Model):
    name = models.CharField(max_length=100, null=False)
    alias = models.CharField(max_length=20, null=False, unique=True,
                             error_messages={
                                 'unique': _("A level of context with that alias already exists."),
                             })
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True)

    # Format str.
    def __str__(self):
        return self.name


# Language
class Language(models.Model):
    name = models.CharField(max_length=100, null=False)
    alias = models.CharField(max_length=20, null=False, unique=True,
                             error_messages={
                                 'unique': _("A language of context with that alias already exists."),
                             })
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True)

    # Format str.
    def __str__(self):
        return self.name


# Context.
class Context(BaseModel):
    alias = models.CharField(max_length=20, null=False, unique=True,
                             error_messages={
                                 'unique': _("A context of this type with that alias already exists."),
                             })
    # Config fiedls.
    type = models.ForeignKey('ContextType', on_delete=models.CASCADE)
    format = models.ForeignKey('Format', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    # Description fields.
    description = models.TextField(max_length=500, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    syllabus = models.TextField(max_length=500, null=True, blank=True)
    requeriments = models.TextField(max_length=500, null=True, blank=True)
    level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    tech_tags = models.CharField(max_length=200, null=True, blank=True)
    # Date config fields.
    start_at = models.DateTimeField(null=False, default=timezone_now)
    end_at = models.DateTimeField(null=False, default=timezone_now)
    # Relations fields.
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    teacher_main = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    # Fields API.
    #
    # Calculate fields.
    @property
    def students_num(self):
        return 5

    # Students
    @property
    def students(self):
        students = []
        student = {'name': 'Sergio'}
        students.append(student)
        student = {'name': 'Marcos'}
        students.append(student)
        return students

    # Teachers
    @property
    def teachers(self):
        teachers = []
        teacher = {'name': 'Laura'}
        teachers.append(teacher)
        return teachers


# Category.
class Category(BaseModel):
    alias = models.CharField(max_length=20, null=False, unique=True,
                             error_messages={
                                 'unique': _("A category with that alias already exists."),
                             })
    description = models.TextField(max_length=200, null=True, blank=True)
    # State fields.
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=False, null=False)
    # Relations fields.
    context_type = models.ForeignKey(ContextType, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
