# Generated by Django 3.0.6 on 2020-05-26 17:34

from django.db import migrations

from django.utils import timezone


# Add Contexts.
def add_contexts(apps, schema_editor):
    context = apps.get_model('manager', 'Context')
    context_object = context(name='Plataforma', alias='platform')
    context_object.save()
    context_object = context(name='Institución', alias='institution')
    context_object.save()
    context_object = context(name='Escuela', alias='school')
    context_object.save()
    context_object = context(name='Grado', alias='grade')
    context_object.save()
    context_object = context(name='Máster', alias='master')
    context_object.save()
    context_object = context(name='Curso', alias='course')
    context_object.save()
    context_object = context(name='Aula', alias='classroom')
    context_object.save()
    context_object = context(name='Sección', alias='section')
    context_object.save()
    context_object = context(name='Ítem', alias='item')
    context_object.save()


# Add States.
def add_states(apps, schema_editor):
    state = apps.get_model('manager', 'State')
    state_object = state(name='Activo', alias='active')
    state_object.save()
    state_object = state(name='Deshabilitado', alias='unactive')
    state_object.save()


# Add Countries.
def add_countries(apps, schema_editor):
    country = apps.get_model('manager', 'Country')
    country_object = country(code='ES', name='España', original_name='España')
    country_object.save()


# Add Provinces.
def add_provinces(apps, schema_editor):
    country = apps.get_model('manager', 'Country')
    country_es = country.objects.get(code='ES')
    province = apps.get_model('manager', 'Province')
    province_object = province(code='01', name='Álava', country=country_es)
    province_object.save()
    province_object = province(code='02', name='Albacete', country=country_es)
    province_object.save()
    province_object = province(code='03', name='Alicante', country=country_es)
    province_object.save()
    province_object = province(code='04', name='Almería', country=country_es)
    province_object.save()
    province_object = province(code='05', name='Ávila', country=country_es)
    province_object.save()
    province_object = province(code='06', name='Badajoz', country=country_es)
    province_object.save()
    province_object = province(code='07', name='Baleares', country=country_es)
    province_object.save()
    province_object = province(code='08', name='Barcelona', country=country_es)
    province_object.save()
    province_object = province(code='09', name='Burgos', country=country_es)
    province_object.save()
    province_object = province(code='10', name='Cáceres', country=country_es)
    province_object.save()
    province_object = province(code='11', name='Cádiz', country=country_es)
    province_object.save()
    province_object = province(code='12', name='Castellón', country=country_es)
    province_object.save()
    province_object = province(code='13', name='Ciudad Real', country=country_es)
    province_object.save()
    province_object = province(code='14', name='Córdoba', country=country_es)
    province_object.save()
    province_object = province(code='15', name='La Coruña', country=country_es)
    province_object.save()
    province_object = province(code='16', name='Cuenca', country=country_es)
    province_object.save()
    province_object = province(code='17', name='Gerona', country=country_es)
    province_object.save()
    province_object = province(code='18', name='Granada', country=country_es)
    province_object.save()
    province_object = province(code='19', name='Guadalajara', country=country_es)
    province_object.save()
    province_object = province(code='20', name='Guipúzcoa', country=country_es)
    province_object.save()
    province_object = province(code='21', name='Huelva', country=country_es)
    province_object.save()
    province_object = province(code='22', name='Huesca', country=country_es)
    province_object.save()
    province_object = province(code='23', name='Jaén', country=country_es)
    province_object.save()
    province_object = province(code='24', name='León', country=country_es)
    province_object.save()
    province_object = province(code='25', name='Lérida', country=country_es)
    province_object.save()
    province_object = province(code='26', name='La Rioja', country=country_es)
    province_object.save()
    province_object = province(code='27', name='Lugo', country=country_es)
    province_object.save()
    province_object = province(code='28', name='Madrid', country=country_es)
    province_object.save()
    province_object = province(code='29', name='Málaga', country=country_es)
    province_object.save()
    province_object = province(code='30', name='Murcia', country=country_es)
    province_object.save()
    province_object = province(code='31', name='Navarra', country=country_es)
    province_object.save()
    province_object = province(code='32', name='Orense', country=country_es)
    province_object.save()
    province_object = province(code='33', name='Asturias', country=country_es)
    province_object.save()
    province_object = province(code='34', name='Palencia', country=country_es)
    province_object.save()
    province_object = province(code='35', name='Las Palmas', country=country_es)
    province_object.save()
    province_object = province(code='36', name='Pontevedra', country=country_es)
    province_object.save()
    province_object = province(code='37', name='Salamanca', country=country_es)
    province_object.save()
    province_object = province(code='38', name='Santa Cruz de Tenerife', country=country_es)
    province_object.save()
    province_object = province(code='39', name='Cantabria', country=country_es)
    province_object.save()
    province_object = province(code='40', name='Segovia', country=country_es)
    province_object.save()
    province_object = province(code='41', name='Sevilla', country=country_es)
    province_object.save()
    province_object = province(code='42', name='Soria', country=country_es)
    province_object.save()
    province_object = province(code='43', name='Tarragona', country=country_es)
    province_object.save()
    province_object = province(code='44', name='Teruel', country=country_es)
    province_object.save()
    province_object = province(code='45', name='Toledo', country=country_es)
    province_object.save()
    province_object = province(code='46', name='Valencia', country=country_es)
    province_object.save()
    province_object = province(code='47', name='Valladolid', country=country_es)
    province_object.save()
    province_object = province(code='48', name='Vizcaya', country=country_es)
    province_object.save()
    province_object = province(code='49', name='Zamora', country=country_es)
    province_object.save()
    province_object = province(code='50', name='Zaragoza', country=country_es)
    province_object.save()
    province_object = province(code='51', name='Ceuta', country=country_es)
    province_object.save()
    province_object = province(code='52', name='Melilla', country=country_es)
    province_object.save()


# Add Languages.
def add_languages(apps, schema_editor):
    language = apps.get_model('manager', 'Language')
    language_object = language(code='es', name='Español')
    language_object.save()
    language_object = language(code='en', name='Inglés')
    language_object.save()


# Add Roles.
def add_roles(apps, schema_editor):
    state = apps.get_model('manager', 'State')
    state_active = state.objects.get(alias='active')
    role = apps.get_model('manager', 'Role')
    role_object = role(name='Estudiante', state=state_active, is_visible=True, icon='user-graduate',
                       alias='student', visible_at=timezone.now(), state_at=timezone.now(),)
    role_object.save()
    role_object = role(name='Profesor', state=state_active, is_visible=True, icon='chalkboard',
                       alias='teacher', visible_at=timezone.now(), state_at=timezone.now(),)
    role_object.save()
    role_object = role(name='Autor', state=state_active, is_visible=True, icon='user-edit',
                       alias='author', visible_at=timezone.now(), state_at=timezone.now(),)
    role_object.save()
    role_object = role(name='Profesor Creador', state=state_active, is_visible=True, icon='chalkboard-teacher',
                       alias='teacherpro', visible_at=timezone.now(), state_at=timezone.now(),)
    role_object.save()
    role_object = role(name='Invitado', state=state_active, is_visible=False, icon='user-secret',
                       alias='guest', visible_at=timezone.now(), state_at=timezone.now(),)
    role_object.save()
    role_object = role(name='Marketing', state=state_active, is_visible=True, icon='user-tag',
                       alias='marketing', visible_at=timezone.now(), state_at=timezone.now(),)
    role_object.save()
    role_object = role(name='Identificado', state=state_active, is_visible=True, icon='user',
                       alias='user', visible_at=timezone.now(), state_at=timezone.now(),)
    role_object.save()
    role_object = role(name='Gestor', state=state_active, is_visible=True, icon='user-cog',
                       alias='manager', visible_at=timezone.now(), state_at=timezone.now(),)
    role_object.save()
    role_object = role(name='Director', state=state_active, is_visible=True, icon='user-tie',
                       alias='director', visible_at=timezone.now(), state_at=timezone.now(),)
    role_object.save()
    role_object = role(name='Secretario', state=state_active, is_visible=True, icon='user-clock',
                       alias='secretary', visible_at=timezone.now(), state_at=timezone.now(),)
    role_object.save()


# Add Permissions.
def add_permissions(apps, schema_editor):
    state = apps.get_model('manager', 'State')
    state_active = state.objects.get(alias='active')
    context = apps.get_model('manager', 'Context')
    context_course = context.objects.get(alias='course')
    permission = apps.get_model('manager', 'Permission')
    permission_object = permission(alias='course-create', description='Crear curso',
                                   state=state_active, is_visible=True, context=context_course,
                                   visible_at=timezone.now(), state_at=timezone.now(),)
    permission_object.save()
    permission_object = permission(alias='course-view', description='Ver curso',
                                   state=state_active, is_visible=True, context=context_course,
                                   visible_at=timezone.now(), state_at=timezone.now(),)
    permission_object.save()


# Add Permissions of Role.
def add_permissions_role(apps, schema_editor):
    role = apps.get_model('manager', 'Role')
    role_student = role.objects.get(alias='student')
    permission = apps.get_model('manager', 'Permission')
    permission_create_course = permission.objects.get(alias='course-create')
    permission_view_course = permission.objects.get(alias='course-view')
    permission_role = apps.get_model('manager', 'PermissionRole')
    permission_role_object = permission_role(role=role_student, permission=permission_create_course,
                                             is_active=True, active_at=timezone.now(),)
    permission_role_object.save()
    permission_role_object = permission_role(role=role_student, permission=permission_view_course,
                                             is_active=True, active_at=timezone.now(),)
    permission_role_object.save()


# Add Users.
def add_users(apps, schema_editor):
    state = apps.get_model('manager', 'State')
    state_active = state.objects.get(alias='active')
    state_unactive = state.objects.get(alias='unactive')
    language = apps.get_model('manager', 'Language')
    language_es = language.objects.get(code='es')
    language_en = language.objects.get(code='en')
    role = apps.get_model('manager', 'Role')
    role_student = role.objects.get(alias='student')
    role_teacherpro = role.objects.get(alias='teacherpro')
    role_teacher = role.objects.get(alias='teacher')
    role_author = role.objects.get(alias='author')
    role_secretary = role.objects.get(alias='secretary')
    role_director = role.objects.get(alias='director')
    province = apps.get_model('manager', 'Province')
    province_madrid = province.objects.get(code='28')
    province_barcelona = province.objects.get(code='08')
    province_sevilla = province.objects.get(code='41')
    province_valencia = province.objects.get(code='46')
    country = apps.get_model('manager', 'Country')
    country_es = country.objects.get(code='ES')
    # Create Users.
    user = apps.get_model('manager', 'UserManager')
    user_object = user(username='amanzanod', password='12345', state=state_active, is_visible=True,
                       name='Antonio', surname1='Manzano', surname2='Díaz', title='Creador Multimedia',
                       email='amanzanod@uoc.edu', province=province_madrid, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/amanzanod.png', about_me='<p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.</p> <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet</p>')
    user_object.save()
    user_object = user(username='mamaga', password='12345', state=state_active, is_visible=True,
                       name='María', surname1='Mata', surname2='García', title='Programador PHP',
                       email='marco@hypotesis.com', province=province_barcelona, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/mamaga.png')
    user_object.save()
    user_object = user(username='rogoag', password='12345', state=state_active, is_visible=True,
                       name='Roberto', surname1='Gómez', surname2='Aguado', title='Creador Multimedia',
                       email='rga@hypotesis.com', province=province_barcelona, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/rogoag.png')
    user_object.save()
    user_object = user(username='jusagu', password='12345', state=state_active, is_visible=True,
                       name='Julieta', surname1='Sanz', surname2='Guardiola', title='Desarrollador Front',
                       email='julsanz@hypotesis.com', province=province_sevilla, country=country_es,
                       role=role_teacherpro, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/jusagu.png')
    user_object.save()
    user_object = user(username='jugamo', password='12345', state=state_active, is_visible=True,
                       name='Juana', surname1='García', surname2='Moreno', title='Psicopedagogo',
                       email='jugamor@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_author, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/jugamo.png')
    user_object.save()
    user_object = user(username='pamaso', password='12345', state=state_active, is_visible=True,
                       name='Patricia', surname1='Martínez', surname2='Soler', title='Graduado ADE',
                       email='pamasol@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_secretary, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/pamaso.png')
    user_object.save()
    user_object = user(username='dapisa', password='12345', state=state_active, is_visible=True,
                       name='David', surname1='Pinilla', surname2='Sala', title='Diseñador Gráfico',
                       email='david78@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/dapisa.png')
    user_object.save()
    user_object = user(username='sijiso', password='12345', state=state_unactive, is_visible=False,
                       name='Silvia', surname1='Jiménez', surname2='Soriano', title='Diseñador Gráfico',
                       email='sxsor@hypotesis.com', province=province_barcelona, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/sijiso.png')
    user_object.save()
    user_object = user(username='magaro', password='12345', state=state_active, is_visible=True,
                       name='Mario', surname1='García', surname2='Rodriguez', title='Software Developer',
                       email='devil29@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_teacherpro, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/magaro.png')
    user_object.save()
    user_object = user(username='remomo', password='12345', state=state_unactive, is_visible=True,
                       name='Rebeca', surname1='Molina', surname2='Montoro', title='Programador Python',
                       email='rebex29@hypotesis.com', province=province_sevilla, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/remomo.png')
    user_object.save()
    user_object = user(username='jomose', password='12345', state=state_unactive, is_visible=True,
                       name='José', surname1='Moreno', surname2='Sevilla', title='Diseñador Gráfico',
                       email='jose.moreno@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/jomose.png')
    user_object.save()
    user_object = user(username='capeto', password='12345', state=state_unactive, is_visible=True,
                       name='Carmen', surname1='Pérez', surname2='Toledo', title='Programador Python',
                       email='capeto@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/capeto.png')
    user_object.save()
    user_object = user(username='sosulo', password='12345', state=state_unactive, is_visible=True,
                       name='Sonia', surname1='Suárez', surname2='López', title='Programador PHP',
                       email='sosulo@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/sosulo.png')
    user_object.save()
    user_object = user(username='tallome', password='12345', state=state_unactive, is_visible=True,
                       name='Tania', surname1='Llorente', surname2='Mena', title='Desarrollador Web',
                       email='tallome@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/tallome.png')
    user_object.save()
    user_object = user(username='ancrune', password='12345', state=state_unactive, is_visible=True,
                       name='Antonio', surname1='Cruz', surname2='Nevado', title='JavaScript Developer',
                       email='ancrune@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/ancrune.png')
    user_object.save()
    user_object = user(username='masago', password='12345', state=state_unactive, is_visible=True,
                       name='Marta', surname1='Sánchez', surname2='Gómez', title='Diseñador Gráfico',
                       email='masago@hypotesis.com', province=province_sevilla, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/masago.png')
    user_object.save()
    user_object = user(username='jusica', password='12345', state=state_unactive, is_visible=True,
                       name='Juan Pablo', surname1='Sierra', surname2='Del Campo', title='Creador Multimedia',
                       email='jusica@hypotesis.com', province=province_valencia, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/jusica.png')
    user_object.save()
    user_object = user(username='moseig', password='12345', state=state_unactive, is_visible=True,
                       name='Mónica', surname1='Serena', surname2='Iglesias', title='Programador Python',
                       email='moseig@hypotesis.com', province=province_valencia, country=country_es,
                       role=role_student, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/moseig.png')
    user_object.save()
    user_object = user(username='blafega', password='12345', state=state_unactive, is_visible=True,
                       name='Blanca', surname1='Fernández', surname2='García', title='Backend Developer',
                       email='blafega@hypotesis.com', province=province_valencia, country=country_es,
                       role=role_teacherpro, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/blafega.png')
    user_object.save()
    user_object = user(username='madiji', password='12345', state=state_unactive, is_visible=True,
                       name='Marco', surname1='Díaz', surname2='Jimenez', title='Software Architect',
                       email='madiji@hypotesis.com', province=province_valencia, country=country_es,
                       role=role_teacher, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/madiji.png')
    user_object.save()
    user_object = user(username='roguma', password='12345', state=state_unactive, is_visible=True,
                       name='Rocío', surname1='Gutierrez', surname2='Martín', title='Experta Pedagógica',
                       email='roguma@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_author, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/roguma.png')
    user_object.save()
    user_object = user(username='mamofe', password='12345', state=state_unactive, is_visible=True,
                       name='Martín', surname1='Moreno', surname2='Fernández', title='Creador de Contenidos',
                       email='mamofe@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_author, language=language_es, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/mamofe.png')
    user_object.save()
    user_object = user(username='mismi', password='12345', state=state_unactive, is_visible=True,
                       name='Michael', surname1='Smith', surname2='', title='Python Master',
                       email='mismi@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_teacher, language=language_en, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/mismi.png')
    user_object.save()
    user_object = user(username='stema', password='12345', state=state_unactive, is_visible=True,
                       name='Steve', surname1='Marion', surname2='', title='HTML5 LAYOUT',
                       email='stema@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_student, language=language_en, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/stema.png')
    user_object.save()
    user_object = user(username='jorope', password='12345', state=state_unactive, is_visible=True,
                       name='José', surname1='Rodriguez', surname2='Pérez', title='Director Escuela',
                       email='jorope@hypotesis.com', province=province_madrid, country=country_es,
                       role=role_director, language=language_en, visible_at=timezone.now(),
                       state_at=timezone.now(), picture='profile/jorope.png')
    user_object.save()


# Migrations.
class Migration(migrations.Migration):
    dependencies = [
        ('manager', '0002_auto_20200526_2146'),
    ]

    operations = [
        migrations.RunPython(add_contexts),
        migrations.RunPython(add_states),
        migrations.RunPython(add_countries),
        migrations.RunPython(add_provinces),
        migrations.RunPython(add_languages),
        migrations.RunPython(add_roles),
        migrations.RunPython(add_permissions),
        migrations.RunPython(add_permissions_role),
        migrations.RunPython(add_users),
    ]

