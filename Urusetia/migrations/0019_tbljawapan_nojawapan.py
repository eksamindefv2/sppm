# Generated by Django 2.0.6 on 2018-12-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Urusetia', '0018_auto_20181211_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbljawapan',
            name='NoJawapan',
            field=models.CharField(default=1, max_length=10, verbose_name='NoJawapan'),
            preserve_default=False,
        ),
    ]
