# Generated by Django 4.1 on 2023-10-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.FileField(upload_to='image')),
            ],
        ),
    ]
