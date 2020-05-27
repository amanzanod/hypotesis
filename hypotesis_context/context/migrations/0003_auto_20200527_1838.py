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
    state_object = state(name='Terminado', alias='finished')
    state_object.save()
    state_object = state(name='Pausado', alias='paused')
    state_object.save()
    state_object = state(name='En creación', alias='creating')
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


# Add Categories.
def add_categories(apps, schema_editor):
    state = apps.get_model('context', 'State')
    state_active = state.objects.get(alias='active')
    context_type = apps.get_model('context', 'ContextType')
    context_type_grade = context_type.objects.get(alias='grade')
    context_type_master = context_type.objects.get(alias='master')
    context_type_course = context_type.objects.get(alias='course')
    category = apps.get_model('context', 'Category')
    category_sistems = category(alias='sistems', name='Sistemas', state=state_active,
                                is_visible=True, context_type=context_type_grade)
    category_sistems.save()
    category_development = category(alias='development', name='Desarrollo', state=state_active,
                                    is_visible=True, context_type=context_type_grade)
    category_development.save()
    category_object = category(alias='cibersecurity', name='Cyberseguridad', state=state_active,
                               is_visible=True, context_type=context_type_grade, parent=category_sistems)
    category_object.save()
    category_object = category(alias='elearning', name='Elearning', state=state_active,
                               is_visible=True, context_type=context_type_grade, parent=category_development)
    category_object.save()
    category_object = category(alias='web', name='Web', state=state_active,
                               is_visible=True, context_type=context_type_grade, parent=category_development)
    category_object.save()
    category_object = category(alias='software', name='Software', state=state_active,
                               is_visible=True, context_type=context_type_grade, parent=category_development)
    category_object.save()
    category_deployment = category(alias='deploy', name='Despliegue', state=state_active,
                                   is_visible=True, context_type=context_type_grade, parent=category_sistems)
    category_deployment.save()
    category_backend = category(alias='backend', name='Backend', state=state_active,
                                is_visible=True, context_type=context_type_master, parent=category_development)
    category_backend.save()
    category_frontend = category(alias='frontend', name='Frontend', state=state_active,
                                 is_visible=True, context_type=context_type_master, parent=category_development)
    category_frontend.save()
    category_cloud = category(alias='cloud', name='Cloud', state=state_active,
                              is_visible=True, context_type=context_type_master, parent=category_sistems)
    category_cloud.save()
    category_object = category(alias='moodle', name='Moodle', state=state_active,
                               is_visible=True, context_type=context_type_master, parent=category_backend)
    category_object.save()
    category_object = category(alias='devops', name='DevOps', state=state_active,
                               is_visible=True, context_type=context_type_master, parent=category_deployment)
    category_object.save()
    category_apirest = category(alias='apirest', name='API Rest', state=state_active,
                               is_visible=True, context_type=context_type_master, parent=category_development)
    category_apirest.save()
    category_object = category(alias='html5', name='HTML5', state=state_active,
                               is_visible=True, context_type=context_type_master, parent=category_frontend)
    category_object.save()
    category_object = category(alias='aws', name='AWS', state=state_active,
                               is_visible=True, context_type=context_type_master, parent=category_cloud)
    category_object.save()
    category_object = category(alias='python', name='Python', state=state_active,
                               is_visible=True, context_type=context_type_master, parent=category_backend)
    category_object.save()
    category_object = category(alias='postman', name='Postman', state=state_active,
                               is_visible=True, context_type=context_type_master, parent=category_apirest)
    category_object.save()
    category_object = category(alias='php', name='PHP', state=state_active,
                               is_visible=True, context_type=context_type_master, parent=category_backend)
    category_object.save()
    category_object = category(alias='docker', name='Docker', state=state_active,
                               is_visible=True, context_type=context_type_master, parent=category_deployment)
    category_object.save()
    category_object = category(alias='ux', name='Usabilidad', state=state_active,
                               is_visible=True, context_type=context_type_master, parent=category_frontend)
    category_object.save()


# Add Platform.
def add_platforms(apps, schema_editor):
    context_type = apps.get_model('context', 'ContextType')
    context_type_platform = context_type.objects.get(alias='platform')
    state = apps.get_model('context', 'State')
    state_active = state.objects.get(alias='active')
    language = apps.get_model('context', 'Language')
    language_es = language.objects.get(code='es')
    context = apps.get_model('context', 'Context')
    platform_object = context(name='Hypotesis PRO', alias='hyppro', state=state_active,
                              type=context_type_platform, language=language_es,)
    platform_object.save()


# Add Schools.
def add_schools(apps, schema_editor):
    context_type = apps.get_model('context', 'ContextType')
    context_type_school = context_type.objects.get(alias='school')
    state = apps.get_model('context', 'State')
    state_active = state.objects.get(alias='active')
    language = apps.get_model('context', 'Language')
    language_es = language.objects.get(code='es')
    context = apps.get_model('context', 'Context')
    platform_object = context(name='Hypotesis School', alias='hypschool', state=state_active,
                              type=context_type_school, language=language_es,)
    platform_object.save()
    platform_object = context(name='Hypotesis Code', alias='hypcode', state=state_active,
                              type=context_type_school, language=language_es,)
    platform_object.save()


# Add Grades.
def add_grades(apps, schema_editor):
    context_type = apps.get_model('context', 'ContextType')
    context_type_grade = context_type.objects.get(alias='grade')
    state = apps.get_model('context', 'State')
    state_active = state.objects.get(alias='active')
    state_finished = state.objects.get(alias='finished')
    language = apps.get_model('context', 'Language')
    language_es = language.objects.get(code='es')
    category = apps.get_model('context', 'Category')
    category_cyber = category.objects.get(alias='cibersecurity')
    category_elearning = category.objects.get(alias='elearning')
    category_web = category.objects.get(alias='web')
    context = apps.get_model('context', 'Context')
    grade_object = context(name='Grado en Ciberseguridad', alias='gcibe', state=state_active,
                           type=context_type_grade, language=language_es, category=category_cyber)
    grade_object.save()
    grade_object = context(name='Grado en e-Learning', alias='gelear', state=state_active,
                           type=context_type_grade, language=language_es, category=category_elearning)
    grade_object.save()
    grade_object = context(name='Grado en Ingeniería Web', alias='ingweb', state=state_finished,
                           type=context_type_grade, language=language_es, category=category_web)
    grade_object.save()


# Add Masters.
def add_masters(apps, schema_editor):
    context_type = apps.get_model('context', 'ContextType')
    context_type_master = context_type.objects.get(alias='master')
    state = apps.get_model('context', 'State')
    state_active = state.objects.get(alias='active')
    state_finished = state.objects.get(alias='finished')
    state_paused = state.objects.get(alias='paused')
    language = apps.get_model('context', 'Language')
    language_es = language.objects.get(code='es')
    category = apps.get_model('context', 'Category')
    category_backend = category.objects.get(alias='backend')
    category_moodle = category.objects.get(alias='moodle')
    category_devops = category.objects.get(alias='devops')
    category_apirest = category.objects.get(alias='apirest')
    category_cyber = category.objects.get(alias='cibersecurity')
    category_software = category.objects.get(alias='software')
    category_aws = category.objects.get(alias='aws')
    category_html5 = category.objects.get(alias='html5')
    context = apps.get_model('context', 'Context')
    master_object = context(name='Master en desarrollo con Python 3', alias='mpyt3', state=state_active,
                            is_visible=True, type=context_type_master, language=language_es, category=category_backend)
    master_object.save()
    master_object = context(name='Master en Moodle para desarrolladores', alias='mmood', state=state_active,
                            is_visible=True, type=context_type_master, language=language_es, category=category_moodle)
    master_object.save()
    master_object = context(name='Master en DevOps', alias='devop', state=state_active,
                            is_visible=True, type=context_type_master, language=language_es, category=category_devops)
    master_object.save()
    master_object = context(name='Master en API Rest multilenguaje', alias='apost', state=state_finished,
                            is_visible=True, type=context_type_master, language=language_es, category=category_apirest)
    master_object.save()
    master_object = context(name='Master en ciberseguridad', alias='mcibs', state=state_paused,
                            is_visible=True, type=context_type_master, language=language_es, category=category_cyber)
    master_object.save()
    master_object = context(name='Master en Ingeniería del Software', alias='ingso', state=state_active,
                            is_visible=False, type=context_type_master, language=language_es, category=category_software)
    master_object.save()
    master_object = context(name='Arquitecto Cloud con AWS', alias='araws', state=state_finished,
                            is_visible=True, type=context_type_master, language=language_es, category=category_aws)
    master_object.save()
    master_object = context(name='Master en Maquetación HTML5', alias='maque', state=state_active,
                            is_visible=True, type=context_type_master, language=language_es, category=category_html5)
    master_object.save()


# Migration
class Migration(migrations.Migration):

    dependencies = [
        ('context', '0002_auto_20200527_1838'),
    ]

    operations = [
        migrations.RunPython(add_context_types),
        migrations.RunPython(add_format),
        migrations.RunPython(add_states),
        migrations.RunPython(add_levels),
        migrations.RunPython(add_languages),
        migrations.RunPython(add_categories),
        migrations.RunPython(add_platforms),
        migrations.RunPython(add_schools),
        migrations.RunPython(add_grades),
        migrations.RunPython(add_masters),
    ]
