# Generated by Django 3.1.6 on 2021-02-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='condition',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
