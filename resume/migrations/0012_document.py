# Generated by Django 4.1.3 on 2023-06-22 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_project_project_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
