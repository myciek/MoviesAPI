# Generated by Django 3.1.3 on 2020-11-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201103_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='DVD',
            new_name='dvd',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='imdbID',
            new_name='imdbid',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='imdbRating',
            new_name='imdbratings',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='imdbVotes',
            new_name='imdbvotes',
        ),
        migrations.AddField(
            model_name='movie',
            name='totalSeasons',
            field=models.TextField(blank=True, max_length=3, null=True),
        ),
    ]
