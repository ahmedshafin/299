# Generated by Django 5.0.4 on 2024-05-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_testuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
