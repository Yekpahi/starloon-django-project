# Generated by Django 3.2.7 on 2021-09-29 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
