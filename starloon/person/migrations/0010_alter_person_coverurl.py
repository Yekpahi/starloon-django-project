# Generated by Django 3.2.7 on 2021-10-10 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_auto_20211009_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='coverUrl',
            field=models.ImageField(null=True, upload_to='person-cover/%Y/%m/%d'),
        ),
    ]
