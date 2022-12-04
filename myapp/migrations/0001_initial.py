# Generated by Django 4.0.4 on 2022-12-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookID', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('authors', models.TextField()),
                ('average_rating', models.FloatField()),
                ('isbn', models.CharField(max_length=12)),
                ('isbn13', models.BigIntegerField()),
                ('language_code', models.CharField(max_length=10)),
                ('num_pages', models.IntegerField()),
                ('ratings_count', models.IntegerField()),
                ('text_reviews_count', models.IntegerField()),
                ('publication_date', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=300)),
            ],
        ),
    ]
