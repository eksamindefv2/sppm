# Generated by Django 2.0.6 on 2018-11-22 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblSesi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Siri', models.CharField(max_length=50, verbose_name='Siri')),
                ('TarikhMula', models.DateField(max_length=60, verbose_name='TarikhMula')),
                ('TarikhTamat', models.DateField(max_length=60, verbose_name='TarikhTamat')),
                ('Status', models.IntegerField(default=1, verbose_name='StatusSesi')),
            ],
        ),
    ]
