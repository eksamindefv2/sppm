# Generated by Django 2.0.6 on 2018-12-11 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Urusetia', '0020_auto_20181211_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbljawapan',
            name='Nilai',
            field=models.IntegerField(default=0, verbose_name='Nilai'),
        ),
    ]
