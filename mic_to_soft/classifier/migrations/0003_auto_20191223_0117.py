# Generated by Django 2.2.7 on 2019-12-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_auto_20191223_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classifier',
            name='model_hash',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
