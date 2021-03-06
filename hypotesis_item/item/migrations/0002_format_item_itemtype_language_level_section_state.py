# Generated by Django 3.0.6 on 2020-06-01 20:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('alias', models.CharField(error_messages={'unique': 'A format of item with that alias already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Format',
                'verbose_name_plural': 'Formats',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('alias', models.CharField(error_messages={'unique': 'A type of item with that alias already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('type', models.CharField(max_length=100, verbose_name='type')),
            ],
            options={
                'verbose_name': 'Item Type',
                'verbose_name_plural': 'Item Types',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(error_messages={'unique': 'A language of item with that code already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='code')),
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
                ('alias', models.CharField(error_messages={'unique': 'A level of item with that alias already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
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
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('alias', models.CharField(error_messages={'unique': 'A state of item with that alias already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('alias', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('course', models.CharField(max_length=100, verbose_name='course')),
                ('order', models.IntegerField(verbose_name='order')),
                ('is_visible', models.BooleanField(default=False, verbose_name='is visible')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='picture')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
                'unique_together': {('course', 'order')},
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('alias', models.CharField(error_messages={'unique': 'A item with that alias already exists.'}, max_length=20, primary_key=True, serialize=False, verbose_name='alias')),
                ('is_visible', models.BooleanField(default=False, verbose_name='is visible')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='picture')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='duration')),
                ('tech_tags', models.CharField(blank=True, max_length=200, null=True, verbose_name='tech tags')),
                ('start_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='start at')),
                ('end_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='end at')),
                ('order', models.IntegerField(verbose_name='order')),
                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='item.Format', verbose_name='format')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Language', verbose_name='language')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.Level', verbose_name='level')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.Section', verbose_name='section')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.State', verbose_name='state')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.ItemType', verbose_name='type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'unique_together': {('section', 'order')},
            },
        ),
    ]
