# Generated by Django 2.1.7 on 2019-03-24 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]