# Generated by Django 3.2.5 on 2021-07-09 03:51

import os

from django.core import serializers
from django.db import migrations

fixture_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'initial_data.json'


def load_fixture(*_):
    fixture_file = os.path.join(fixture_dir, fixture_filename)

    fixture = open(fixture_file, 'rb')
    objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
    for obj in objects:
        obj.save()
    fixture.close()


def unload_fixture(apps, *_):
    "Brutally deleting all entries for this model..."

    user = apps.get_model("users", "User")
    user.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]