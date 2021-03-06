# Generated by Django 3.0.6 on 2020-05-27 18:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('context', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('alias', models.CharField(error_messages={'unique': 'A category with that alias already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='description')),
                ('is_visible', models.BooleanField(default=False, verbose_name='is visible')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('visible_at', models.DateTimeField(blank=True, null=True, verbose_name='visible at')),
                ('state_at', models.DateTimeField(blank=True, null=True, verbose_name='state at')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContextType',
            fields=[
                ('alias', models.CharField(error_messages={'unique': 'A type of context with that alias already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Context Type',
                'verbose_name_plural': 'Context Types',
            },
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('alias', models.CharField(error_messages={'unique': 'A format of context with that alias already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Format',
                'verbose_name_plural': 'Formats',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(error_messages={'unique': 'A language of context with that code already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='code')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('alias', models.CharField(error_messages={'unique': 'A level of context with that alias already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('alias', models.CharField(error_messages={'unique': 'A state of context with that alias already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('alias',
                 models.CharField(error_messages={'unique': 'A context of this type with that alias already exists.'},
                                  max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='context.ContextType', verbose_name='type')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                             to='context.Context', verbose_name='parent')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='context.State',
                                            verbose_name='state')),
                ('is_visible', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               to='context.Category', verbose_name='category')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='picture')),
                ('syllabus', models.TextField(blank=True, max_length=500, null=True, verbose_name='syllabus')),
                ('requeriments', models.TextField(blank=True, max_length=500, null=True, verbose_name='requeriments')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='duration')),
                ('tech_tags', models.CharField(blank=True, max_length=200, null=True, verbose_name='tech tags')),
                ('start_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='start at')),
                ('end_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='end at')),
                ('teacher_main', models.CharField(blank=True, max_length=200, null=True, verbose_name='teacher main')),

                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='context.Format', verbose_name='format')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='context.Language', verbose_name='language')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='context.Level', verbose_name='level')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('visible_at', models.DateTimeField(blank=True, null=True, verbose_name='visible at')),
                ('state_at', models.DateTimeField(blank=True, null=True, verbose_name='state at')),
            ],
            options={
                'verbose_name': 'Context',
                'verbose_name_plural': 'Contexts',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='context_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='context.ContextType', verbose_name='type'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='context.Category', verbose_name='parent'),
        ),
        migrations.AddField(
            model_name='category',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='context.State', verbose_name='state'),
        ),
    ]
