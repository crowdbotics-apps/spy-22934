# Generated by Django 2.2.17 on 2020-11-24 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=100)),
                ('photo', models.URLField()),
                ('status', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('is_verified', models.BooleanField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_verified', models.DateTimeField()),
                ('sent_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verificationcode_sent_to', to='chat_user_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_blocked', models.BooleanField()),
                ('is_favorite', models.BooleanField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_added_by', to=settings.AUTH_USER_MODEL)),
                ('added_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_added_profile', to='chat_user_profile.Profile')),
            ],
        ),
    ]
