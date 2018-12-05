# Generated by Django 2.0.6 on 2018-12-05 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pentadbir', '0004_uperanan'),
        ('Urusetia', '0009_auto_20181205_1508'),
        ('Penilaian', '0006_auto_20181205_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblPenilaian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Markah', models.FloatField(max_length=50, verbose_name='Markah')),
                ('TarikhPenilaian', models.DateField(max_length=60, verbose_name='TarikhPenilaian')),
                ('Catatan', models.CharField(max_length=50, verbose_name='Catatan')),
                ('AttachmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Penilaian.TblAttachment')),
                ('JadualID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Penilaian.TblJadual')),
                ('PenggunaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pentadbir.UProfil')),
                ('SoalanID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Urusetia.TblSoalan')),
            ],
        ),
    ]