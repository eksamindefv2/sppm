from django.db import models
import Pentadbir

# Create your models here.
class TblSesi(models.Model):
	Siri = models.CharField('Siri',max_length=50,blank=False,null=False)
	TarikhMula = models.DateField('TarikhMula',max_length=60,blank=False,null=False)
	TarikhTamat = models.DateField('TarikhTamat',max_length=60,blank=False,null=False)
	Status = models.IntegerField('StatusSesi',blank=False,null=False, default=1)
	SistemID = models.ForeignKey('Pentadbir.TblSistem',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)


class TblSkala(models.Model):
	Deskripsi = models.CharField('Deskripsi',max_length=50,blank=False,null=False)
	NilaiSkala = models.IntegerField('NilaiSkala',blank=False,null=False, default=1)

	def __str__(self):
		return str(self.pk)


class TblKomponen(models.Model):
	KodKomponen = models.CharField('KodKomponen',max_length=10,blank=False,null=False)
	NamaKomponen = models.CharField('NamaKomponen',max_length=60,blank=False,null=False)
	Pemberat = models.IntegerField('Pemberat',blank=False,null=False, default=0)
	SesiID = models.ForeignKey('TblSesi',on_delete=models.CASCADE)


	def __str__(self):
		return self.KodKomponen


class TblSubKomponen(models.Model):
	SubKodKomponen = models.CharField('SubKodKomponen',max_length=10,blank=False,null=False)
	NamaSubKomponen = models.CharField('NamaSubKomponen',max_length=100,blank=False,null=False)
	Pemberat = models.IntegerField('Pemberat',blank=False,null=False, default=0)
	KomponenID = models.ForeignKey('TblKomponen',on_delete=models.CASCADE)
	SkalaID = models.ForeignKey('TblSkala',on_delete=models.CASCADE)


	def __str__(self):
		return self.KodKomponen
