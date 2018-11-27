from django.shortcuts import render
from .models import TblSistem
from .forms import TblSistemForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
import pyodbc

# Create your views here.
def SenaraiSistem(request):
    # List of records

    # Query from MCDB#####################################################
 #    posts = []
 #    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
	#                       "Server=10.101.1.100;"
	#                       "Database=MCDB;"
	#                       "uid=sa;pwd=cdbdev@2017")
 #    cursor = cnxn.cursor()
 #    cursor.execute('SELECT * FROM TblPersonel')
    
 #    for obj in cursor.fetchall():
 #    	posts.append({"IC": obj[0], "Nama": obj[3]})
	# # context = {'all_posts':cursor.fetchall()}


 #    print(posts)

    # Query from MCDB######################################################


    # for row in cursor:
    # 	print('row = %r' % (row,))

    a = TblSistem.objects.all().order_by('NamaSistem')
    print(a)
    # return render(request,'Pentadbir/sistem.html',{ 'sistem': a,'posts':posts})
    return render(request,'Pentadbir/sistem.html',{ 'sistem': a})


def Sistem_new(request):
	if request.method == "POST":
		request.POST = request.POST.copy()
		form = TblSistemForm(request.POST)

		if form.is_valid():
			sistem = form.save(commit=False)
			sistem.save()
			messages.success(request, 'Sistem berjaya ditambah!')
			return redirect(reverse_lazy('sistem_home'))
	else:
		form = TblSistemForm()
	return render(request, 'Pentadbir/sistem_new.html', {'form': form})