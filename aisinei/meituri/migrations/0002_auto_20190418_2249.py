# Generated by Django 2.1.7 on 2019-04-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meituri', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meituripic',
            name='picname',
            field=models.CharField(max_length=200),
        ),
    ]
