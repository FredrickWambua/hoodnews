# Generated by Django 3.2.7 on 2021-09-30 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210930_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': 'Business', 'verbose_name_plural': 'Businesses'},
        ),
    ]