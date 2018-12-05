# Generated by Django 2.0.6 on 2018-12-05 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Urusetia', '0009_auto_20181205_1508'),
        ('Pentadbir', '0004_uperanan'),
        ('Penilaian', '0003_tbljadual'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblCatatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Catatan', models.CharField(max_length=50, verbose_name='Catatan')),
                ('TarikhTransaksi', models.DateField(max_length=60, verbose_name='TarikhTransaksi')),
                ('Tindakan', models.IntegerField(default=1, verbose_name='Tindakan')),
                ('JadualID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Penilaian.TblJadual')),
                ('PenggunaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pentadbir.UProfil')),
                ('SubKomponenID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Urusetia.TblSubKomponen')),
            ],
        ),
        migrations.AddField(
            model_name='tbljadual',
            name='CatatanID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Penilaian.TblCatatan'),
            preserve_default=False,
        ),
    ]
