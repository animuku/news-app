# Generated by Django 3.1.5 on 2021-03-31 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_article_url_to_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url_to_image',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
