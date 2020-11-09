# Generated by Django 3.1.3 on 2020-11-08 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RestRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('method', models.CharField(choices=[('GET', 'Get'), ('HEAD', 'Head'), ('POST', 'Post'), ('UPDATE', 'Update'), ('PATCH', 'Patch'), ('DELETE', 'Delete')], max_length=6)),
                ('url', models.URLField()),
                ('payload', models.JSONField(blank=True, null=True)),
                ('started', models.DateTimeField(blank=True, null=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RestResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status_code', models.PositiveSmallIntegerField()),
                ('headers', models.JSONField(null=True)),
                ('data', models.JSONField(null=True)),
                ('rest_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.restrequest')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]