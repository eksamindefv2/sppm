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
		return str(self.pk)


class TblSubKomponen(models.Model):
	SubKodKomponen = models.CharField('SubKodKomponen',max_length=10,blank=False,null=False)
	NamaSubKomponen = models.CharField('NamaSubKomponen',max_length=100,blank=False,null=False)
	Pemberat = models.IntegerField('Pemberat',blank=False,null=False, default=0)
	KomponenID = models.ForeignKey('TblKomponen',on_delete=models.CASCADE)
	SkalaID = models.ForeignKey('TblSkala',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)

class TblSoalan(models.Model):
	NoSoalan = models.CharField('NoSoalan',max_length=10,blank=False,null=False)
	DeskripsiSoalan = models.CharField('DeskripsiSoalan',max_length=100,blank=False,null=False)
	Status = models.IntegerField('Statussoalan',blank=False,null=False, default=1)
	KomponenID = models.ForeignKey('TblKomponen',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)


class TblJawapan(models.Model):
	DeskripsiJawapan = models.CharField('DeskripsiJawapan',max_length=100,blank=False,null=False)
	SoalanID = models.ForeignKey('TblSoalan',on_delete=models.CASCADE)
	SkalaID = models.ForeignKey('TblSkala',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)

class TblAuditee(models.Model):
	NamaAuditee = models.CharField('NamaAuditee',max_length=100,blank=False,null=False)
	IDStatus = models.IntegerField('IDStatusAuditee',blank=False,null=False, default=1)

	def __str__(self):
		return str(self.pk)

class TblSubAuditee(models.Model):
	NamaSubAuditee = models.CharField('NamaSubAuditee',max_length=100,blank=False,null=False)
	AuditeeID = models.ForeignKey('TblAuditee',on_delete=models.CASCADE)
	IDStatus = models.IntegerField('IDStatusSubAuditee',blank=False,null=False, default=1)

	def __str__(self):
		return str(self.pk)		
