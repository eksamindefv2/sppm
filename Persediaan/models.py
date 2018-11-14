from django.db import models

# Create your models here.
class TblSistem(models.Model):
	NamaSistem = models.CharField('NamaSistem',max_length=200,blank=False,null=False)
	Tahun = models.IntegerField('Tahun',null=False)
	Status = models.IntegerField('Status',null=False,default=1)
	PemilikSistem = models.CharField('PemilikSistem',max_length=200,null=False)

	def __str__(self):
		return str(self.pk)