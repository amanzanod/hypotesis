from django.db import models
from django.utils.timezone import now as timezone_now
from django.utils.translation import gettext_lazy as _


# Base Model.
class BaseModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    # Date fields.
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        abstract = True
        app_label = 'context'

    # Format str.
    def __str__(self):
        return self.name


# Context.
class ContextAbstract(BaseModel):
    description = models.TextField(max_length=500, null=True, blank=True)
    alias = models.CharField(max_length=20, null=False, unique=True)
    # State fields.
    state = models.SmallIntegerField(default=0, null=False)

    # Meta
    class Meta:
        abstract = True


# Context.
class Context(BaseModel):
    type = models.CharField(max_length=20)
    context_id = models.IntegerField()

    # Meta
    class Meta:
        unique_together = ('type', 'context_id',)


# ContextLevel.
class ContextLevel(ContextAbstract):
    # Description fields.
    picture = models.ImageField(null=True, blank=True)
    syllabus = models.TextField(max_length=500, null=True, blank=True)
    requeriments = models.TextField(max_length=500, null=True, blank=True)
    level = models.CharField(max_length=50, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    tech_tags = models.CharField(max_length=200, null=True, blank=True)
    # Date config fields.
    start_at = models.DateTimeField(null=False, default=timezone_now)
    end_at = models.DateTimeField(null=False, default=timezone_now)
    # Relations fields.
    teacher_main = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    # Calculate fields.
    @property
    def students_num(self):
        return 5

    # Students
    # Teachers

    # Meta
    class Meta:
        abstract = True


# Grade.
class Grade(ContextLevel):
    pass
    # Masters
    # Courses


# Master.
class Master(ContextLevel):
    pass
    # Courses


# Course.
class Course(ContextLevel):
    # Config fiedls.
    format = models.CharField(max_length=50)

    # Classrooms
    # Sections


# Classroom.
class Classroom(ContextLevel):
    # Relations fields.
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)


# Section.
class Section(ContextLevel):
    # Relations fields.
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)


# Category.
class Category(BaseModel):
    state = models.SmallIntegerField(default=0, null=False)
    is_visible = models.BooleanField(default=False, null=False)
    alias = models.CharField(max_length=20, null=False, unique=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    # Relations fields.
    context = models.ForeignKey(Context, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
