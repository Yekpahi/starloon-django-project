# Generated by Django 3.2.7 on 2021-10-08 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('person', '0005_auto_20211007_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='person',
            name='likes',
        ),
        migrations.AddField(
            model_name='person',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Unlike', 'Unlike'), ('like', 'Like')], default='like', max_length=10)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
