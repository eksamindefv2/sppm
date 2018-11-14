from django.shortcuts import render
from .models import TblSistem

# Create your views here.
def SenaraiSistem(request):
    # List of records
    a = TblSistem.objects.all().order_by('NamaSistem')
    print(a)
    return render(request,'Persediaan/sistem.html',{ 'sistem': a })