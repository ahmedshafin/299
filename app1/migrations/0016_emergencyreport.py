# Generated by Django 5.0.4 on 2024-05-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_assignedteam_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='emergencyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('phoneNumber', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
    ]