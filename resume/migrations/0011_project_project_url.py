# Generated by Django 4.1.3 on 2022-12-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_remove_project_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]