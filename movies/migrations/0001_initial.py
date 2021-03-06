# Generated by Django 3.1.3 on 2020-11-03 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('year', models.TextField(max_length=4)),
                ('rated', models.TextField(max_length=5)),
                ('released', models.TextField(max_length=17)),
                ('runtime', models.TextField(max_length=8)),
                ('genre', models.TextField(max_length=255)),
                ('director', models.TextField(max_length=255)),
                ('writer', models.TextField(max_length=255)),
                ('actors', models.TextField(max_length=255)),
                ('plot', models.TextField(max_length=511)),
                ('language', models.TextField(max_length=255)),
                ('country', models.TextField(max_length=255)),
                ('awards', models.TextField(max_length=255)),
                ('poster', models.TextField(max_length=511)),
                ('metascore', models.TextField(max_length=3)),
                ('imdbRating', models.TextField(max_length=3)),
                ('imdbVotes', models.TextField(max_length=12)),
                ('imdbID', models.TextField(max_length=255)),
                ('type', models.TextField(max_length=255)),
                ('DVD', models.TextField(max_length=255)),
                ('boxOffice', models.TextField(max_length=255)),
                ('production', models.TextField(max_length=12)),
                ('website', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField(max_length=255)),
                ('value', models.TextField(max_length=255)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movies.movie')),
            ],
        ),
    ]
