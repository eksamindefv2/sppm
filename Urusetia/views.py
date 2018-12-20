from django.shortcuts import render
from .models import Sesi
from .forms import SesiForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
import pyodbc


# Create your views here.
def SenaraiSesi(request):
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

    a = Sesi.objects.all().order_by('Siri')
    print(a)
    # return render(request,'Pentadbir/sistem.html',{ 'sistem': a,'posts':posts})
    return render(request, 'Urusetia/sesi.html', {'sesi': a})

def TambahSesi(request):
    if request.method == "POST":
        request.POST = request.POST.copy()
        form = SesiForm(request.POST)

        if form.is_valid():
            sesi = form.save(commit=False)
            sesi.save()
            messages.success(request, 'Sesi berjaya ditambah!')
            return redirect(reverse_lazy('sesi_home'))
    else:
        form = SesiForm()
    return render(request, 'Urusetia/sesi_new.html', {'form': form})


def EditSesi(request,pk):
    sesi = get_object_or_404(Sesi, pk=pk)

    if request.method == "POST":

        form = SesiForm(request.POST, instance=sesi)  # value akan submit ke form

        if form.is_valid():  # validate semak semua dah isi
            sesi = form.save(commit=False)  # simpan dalam memori
            sesi.save()  # save ke db
            return redirect(reverse_lazy('sesi_home'))
        # print("POST DAH MASUK") 							#ini macam echo nak semak masuk POST ke x


    else:
        form = SesiForm(instance=sesi)  # yang ni dapatkan id untuk papar
        # print(form)

    return render(request, 'Urusetia/sesi_edit.html', {'form': form})
