# Generated by Django 2.0.6 on 2018-12-05 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Penilaian', '0007_tblpenilaian'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblTambahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Catatan', models.CharField(max_length=50, verbose_name='Catatan')),
                ('AttachmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Penilaian.TblAttachment')),
                ('JadualID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Penilaian.TblJadual')),
            ],
        ),
    ]