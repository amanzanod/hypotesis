from django.contrib import admin

from .models import Context, Grade, Master, Course, Classroom, Category, Section


# Grade Admin.
class GradeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'state_at', 'visible_at')


# Master Admin.
class MasterAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'state_at', 'visible_at')


# Course Admin.
class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'state_at', 'visible_at')


# Classroom Admin.
class ClassroomAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


# Category Admin.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'state_at', 'visible_at')


# Section Admin.
class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'state_at', 'visible_at')


# Register your models here.
admin.site.register(Context)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Section, SectionAdmin)