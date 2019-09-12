# Generated by Django 2.2.5 on 2019-09-12 08:21

import apps.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('social_network', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator])),
                ('sex', models.SmallIntegerField(choices=[(0, 'Unknown'), (1, 'Male'), (2, 'Female')], default=0)),
                ('avatar', models.FileField(blank=True, null=True, upload_to='avatar/%Y/%m/%d/')),
                ('is_online', models.BooleanField(default=False, verbose_name='Online')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_city', to='location.City')),
                ('social_network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_social_network', to='social_network.SocialNetwork')),
            ],
            options={
                'verbose_name': 'Friend',
                'verbose_name_plural': 'Friends',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=100)),
                ('avatar', models.FileField(blank=True, null=True, upload_to='avatar/%Y/%m/%d/')),
                ('sex', models.SmallIntegerField(choices=[(0, 'Unknown'), (1, 'Male'), (2, 'Female')], default=0)),
                ('relationship_status', models.SmallIntegerField(choices=[(0, 'Single'), (1, 'In a relationship'), (2, 'Married')], default=0)),
                ('is_online', models.BooleanField(default=False, verbose_name='Online')),
                ('is_update', models.BooleanField(default=False)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_city', to='location.City')),
                ('friend', models.ManyToManyField(blank=True, related_name='users_friend', to='users.Friend')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('social_network', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_social_network', to='social_network.SocialNetwork')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', apps.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staffs',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.users',),
            managers=[
                ('objects', apps.auth.models.UserManager()),
            ],
        ),
    ]
