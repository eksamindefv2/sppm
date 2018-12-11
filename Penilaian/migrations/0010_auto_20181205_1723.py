# Generated by Django 2.0.6 on 2018-12-05 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Urusetia', '0009_auto_20181205_1508'),
        ('Penilaian', '0009_tblpantau_tblreftambahan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbltambahan',
            name='JadualID',
        ),
        migrations.AddField(
            model_name='tblpenilaian',
            name='TambahanID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Penilaian.TblTambahan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbltambahan',
            name='SesiID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Urusetia.TblSesi'),
            preserve_default=False,
        ),
    ]
