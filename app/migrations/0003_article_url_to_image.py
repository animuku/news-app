# Generated by Django 3.1.5 on 2021-03-31 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210330_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url_to_image',
            field=models.CharField(default='www.google.com', max_length=10000),
            preserve_default=False,
        ),
    ]
