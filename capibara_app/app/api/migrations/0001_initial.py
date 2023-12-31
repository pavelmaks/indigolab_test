# Generated by Django 4.2.7 on 2023-11-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capibara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('capibara_format', models.CharField(max_length=255, verbose_name='capibara_format')),
                ('capibara_slang', models.CharField(max_length=255, verbose_name='capibara_slang')),
                ('capibara_phrases', models.JSONField(verbose_name='capibara_phrases')),
            ],
            options={
                'verbose_name': 'capibara',
                'verbose_name_plural': 'capybaras',
                'db_table': 'capibara',
            },
        ),
    ]
