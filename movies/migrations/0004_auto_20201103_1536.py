# Generated by Django 3.1.3 on 2020-11-03 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20201103_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='imdbratings',
            new_name='imdbrating',
        ),
    ]