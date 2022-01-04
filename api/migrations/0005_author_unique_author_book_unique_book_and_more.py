# Generated by Django 4.0 on 2022-01-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_tracker'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='author',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_author'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_book'),
        ),
        migrations.AddConstraint(
            model_name='genre',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_genre'),
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_tag'),
        ),
        migrations.AddConstraint(
            model_name='tracker',
            constraint=models.UniqueConstraint(fields=('user', 'book'), name='unique_tracker'),
        ),
    ]