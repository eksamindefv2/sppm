# Generated by Django 2.0.6 on 2018-12-05 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Urusetia', '0009_auto_20181205_1508'),
        ('Pentadbir', '0004_uperanan'),
        ('Penilaian', '0008_tbltambahan'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblPantau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AuditeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Urusetia.TblAuditee')),
                ('PenggunaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pentadbir.UProfil')),
            ],
        ),
        migrations.CreateModel(
            name='TblRefTambahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Keterangan', models.CharField(max_length=50, verbose_name='Catatan')),
            ],
        ),
    ]