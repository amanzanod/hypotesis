# Generated by Django 3.0.6 on 2020-05-26 21:46

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('alias', models.CharField(error_messages={'unique': 'A context with that alias already exists.'}, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(error_messages={'unique': 'A country with that code already exists.'}, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('original_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(error_messages={'unique': 'A language of with that code already exists.'}, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('alias', models.CharField(error_messages={'unique': 'A permission with that alias already exists.'}, max_length=20, primary_key=True, serialize=False)),
                ('is_visible', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('visible_at', models.DateTimeField(blank=True, null=True)),
                ('state_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Context')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PermissionRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active_at', models.DateTimeField(blank=True, null=True)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('code', models.CharField(error_messages={'unique': 'A province with that code already exists.'}, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('original_name', models.CharField(max_length=100, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('alias', models.CharField(error_messages={'unique': 'A role with that alias already exists.'}, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_visible', models.BooleanField(default=False)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('visible_at', models.DateTimeField(blank=True, null=True)),
                ('state_at', models.DateTimeField(blank=True, null=True)),
                ('permissions', models.ManyToManyField(blank=True, through='manager.PermissionRole', to='manager.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('alias', models.CharField(error_messages={'unique': 'A state with that alias already exists.'}, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserManager',
            fields=[
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, primary_key=True, serialize=False, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to='manager.Role')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.State')),
                ('is_visible', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('surname1', models.CharField(max_length=100)),
                ('surname2', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.Province')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.Country')),
                ('about_me', models.TextField(blank=True, max_length=500, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.Language')),
                ('visible_at', models.DateTimeField(blank=True, null=True)),
                ('state_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('password', models.CharField(max_length=100)),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='role',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.State'),
        ),
        migrations.AddField(
            model_name='permissionrole',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Role'),
        ),
        migrations.AddField(
            model_name='permission',
            name='roles',
            field=models.ManyToManyField(blank=True, through='manager.PermissionRole', to='manager.Role'),
        ),
        migrations.AddField(
            model_name='permission',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.State'),
        ),
        migrations.AlterUniqueTogether(
            name='permissionrole',
            unique_together={('role', 'permission')},
        ),
    ]
