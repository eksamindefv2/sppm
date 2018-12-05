from django.db import models
import Pentadbir,Urusetia


# Create your models here.
class TblRefStatusPenilaian(models.Model):
	StatusPenilaian = models.CharField('StatusPenilaian',max_length=50,blank=False,null=False)
	Keterangan = models.CharField('Keterangan',max_length=50,blank=False,null=False)
	Status = models.IntegerField('Status',blank=False,null=False, default=1)

	def __str__(self):
		return str(self.pk)

class TblJadual(models.Model):
	TarikhMula = models.DateField('TarikhMula',max_length=60,blank=False,null=False)
	TarikhTamat = models.DateField('TarikhTamat',max_length=60,blank=False,null=False)
	Status = models.IntegerField('Status',blank=False,null=False, default=1)
	SesiID = models.ForeignKey('Urusetia.TblSesi',on_delete=models.CASCADE)
	AuditeeID = models.ForeignKey('Urusetia.TblAuditee',on_delete=models.CASCADE)
	PenggunaID = models.ForeignKey('Pentadbir.UProfil',on_delete=models.CASCADE)
	StatusPenilaianID = models.ForeignKey('TblRefStatusPenilaian',on_delete=models.CASCADE)
	CatatanID = models.ForeignKey('TblCatatan',on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.pk)


class TblAuditTrailJadual(models.Model):
	TarikhTransaksi = models.DateField('TarikhTransaksi',max_length=60,blank=False,null=False)
	Tindakan = models.CharField('Tindakan',max_length=50,blank=False,null=False)
	JadualID = models.ForeignKey('TblJadual',on_delete=models.CASCADE)
	PenggunaID = models.ForeignKey('Pentadbir.UProfil',on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.pk)


class TblCatatan(models.Model):
	Catatan = models.CharField('Catatan',max_length=50,blank=False,null=False)
	TarikhTransaksi = models.DateField('TarikhTransaksi',max_length=60,blank=False,null=False)
	Tindakan = models.IntegerField('Tindakan',blank=False,null=False, default=1)
	JadualID = models.ForeignKey('TblJadual',on_delete=models.CASCADE)
	PenggunaID = models.ForeignKey('Pentadbir.UProfil',on_delete=models.CASCADE)
	SubKomponenID = models.ForeignKey('Urusetia.TblSubKomponen',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)


class TblAttachment(models.Model):
	DeskripsiAttachment = models.CharField('DeskripsiAttachment',max_length=50,blank=False,null=False)
	Path = models.CharField('Path',max_length=50,blank=False,null=False)
	JenisKategoriID = models.ForeignKey('TblRefAttachment',on_delete=models.CASCADE)


	def __str__(self):
		return str(self.pk)



class TblRefAttachment(models.Model):
	JenisKategori = models.CharField('JenisKategori',max_length=50,blank=False,null=False)

	def __str__(self):
		return str(self.pk)		


class TblPenilaian(models.Model):
	Markah = models.FloatField('Markah',max_length=50,blank=False,null=False)
	TarikhPenilaian = models.DateField('TarikhPenilaian',max_length=60,blank=False,null=False)
	Catatan = models.CharField('Catatan',max_length=50,blank=False,null=False)
	SoalanID = models.ForeignKey('Urusetia.TblSoalan',on_delete=models.CASCADE)
	JadualID = models.ForeignKey('TblJadual',on_delete=models.CASCADE)
	PenggunaID = models.ForeignKey('Pentadbir.UProfil',on_delete=models.CASCADE)
	AttachmentID = models.ForeignKey('TblAttachment',on_delete=models.CASCADE)


	def __str__(self):
		return str(self.pk)


class TblTambahan(models.Model):
	Catatan = models.CharField('Catatan',max_length=50,blank=False,null=False)
	AttachmentID = models.ForeignKey('TblAttachment',on_delete=models.CASCADE)
	JadualID = models.ForeignKey('TblJadual',on_delete=models.CASCADE)


	def __str__(self):
		return str(self.pk)

class TblRefTambahan(models.Model):
	Keterangan = models.CharField('Catatan',max_length=50,blank=False,null=False)


	def __str__(self):
		return str(self.pk)


class TblPantau(models.Model):
	PenggunaID = models.ForeignKey('Pentadbir.UProfil',on_delete=models.CASCADE)
	AuditeeID = models.ForeignKey('Urusetia.TblAuditee',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.pk)