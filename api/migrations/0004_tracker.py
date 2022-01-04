# Generated by Django 4.0 on 2022-01-04 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_tracker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WANT', 'Want to Read'), ('READ', 'Currently Reading'), ('DONE', 'Finished Reading')], default='WANT', max_length=4)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracker', to='api.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracker', to='api.user')),
            ],
        ),
    ]