# Generated by Django 3.0.6 on 2020-05-27 18:14

from django.db import migrations
from django.utils import timezone


# Add Context Types.
def add_context_types(apps, schema_editor):
    context_type = apps.get_model('context', 'ContextType')
    context_type_object = context_type(name='Plataforma', alias='platform')
    context_type_object.save()
    context_type_object = context_type(name='Institución', alias='institution')
    context_type_object.save()
    context_type_object = context_type(name='Escuela', alias='school')
    context_type_object.save()
    context_type_object = context_type(name='Grado', alias='grade')
    context_type_object.save()
    context_type_object = context_type(name='Máster', alias='master')
    context_type_object.save()
    context_type_object = context_type(name='Curso', alias='course')
    context_type_object.save()
    context_type_object = context_type(name='Aula', alias='classroom')
    context_type_object.save()
    context_type_object = context_type(name='Sección', alias='section')
    context_type_object.save()
    context_type_object = context_type(name='Ítem', alias='item')
    context_type_object.save()


# Add Format.
def add_format(apps, schema_editor):
    format_context = apps.get_model('context', 'Format')
    format_object = format_context(name='Temas', alias='topics')
    format_object.save()
    format_object = format_context(name='Semanas', alias='weeks')
    format_object.save()
    format_object = format_context(name='Días', alias='days')
    format_object.save()


# Add States.
def add_states(apps, schema_editor):
    state = apps.get_model('context', 'State')
    state_object = state(name='Activo', alias='active')
    state_object.save()
    state_object = state(name='Deshabilitado', alias='unactive')
    state_object.save()


# Add Levels.
def add_levels(apps, schema_editor):
    level = apps.get_model('context', 'Level')
    level_object = level(name='Principiante', alias='beginner')
    level_object.save()
    level_object = level(name='Medio', alias='medium')
    level_object.save()
    level_object = level(name='Avanzado', alias='advanced')
    level_object.save()
    level_object = level(name='Experto', alias='expert')
    level_object.save()
    level_object = level(name='Profesional', alias='professional')
    level_object.save()


# Add Languages.
def add_languages(apps, schema_editor):
    language = apps.get_model('context', 'Language')
    language_object = language(code='es', name='Español')
    language_object.save()
    language_object = language(code='en', name='Inglés')
    language_object.save()


# Add Platform.
def add_platforms(apps, schema_editor):
    context_type = apps.get_model('context', 'ContextType')
    context_type_platform = context_type.objects.get(alias='platform')
    state = apps.get_model('context', 'State')
    state_active = state.objects.get(alias='active')
    context = apps.get_model('context', 'Context')
    platform_object = context(name='Hypotesis PRO', alias='hypotesis', state=state_active,
                              type=context_type_platform, )
    platform_object.save()


# Migration
class Migration(migrations.Migration):

    dependencies = [
        ('context', '0002_auto_20200527_1814'),
    ]

    operations = [
        migrations.RunPython(add_context_types),
        migrations.RunPython(add_format),
        migrations.RunPython(add_states),
        migrations.RunPython(add_levels),
        migrations.RunPython(add_languages),
        migrations.RunPython(add_platforms),
    ]
