# Generated by Django 4.2.2 on 2023-07-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
