# Generated by Django 3.1.5 on 2021-03-31 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sources',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
