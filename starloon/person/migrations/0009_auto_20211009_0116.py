# Generated by Django 3.2.7 on 2021-10-08 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0008_alter_like_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='liked',
        ),
        migrations.AlterField(
            model_name='person',
            name='coverUrl',
            field=models.ImageField(null=True, upload_to='person-cover'),
        ),
        migrations.AlterField(
            model_name='person',
            name='personImage',
            field=models.ImageField(null=True, upload_to='person-profile'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]