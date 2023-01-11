# Generated by Django 4.1.5 on 2023-01-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('data', models.DateField()),
                ('description', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]