# Generated by Django 2.2.7 on 2019-11-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.CharField(max_length=100)),
                ('PASSWORD', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
            ],
        ),
    ]