# Generated by Django 4.1.1 on 2022-10-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0004_newregister2_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=130)),
                ('email', models.CharField(max_length=130)),
                ('textarea', models.CharField(max_length=130)),
                ('date', models.DateField()),
            ],
        ),
    ]
