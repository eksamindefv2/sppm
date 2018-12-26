from django.shortcuts import render
from .models import Sistem, RefPeranan
from .forms import SistemForm, RefPerananForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
import pyodbc

# Create your views here.


def SenaraiSistem(request):
    a = Sistem.objects.all().order_by('NamaSistem')
    return render(request, 'Pentadbir/sistem.html', {'sistem': a})


def Sistem_new(request):

    #Check form dah disubmit atau belum
    if request.method == "POST":
        form = SistemForm(request.POST)

        #Check
        if form.is_valid():
            sistem = form.save(commit=False)
            sistem.save()
            messages.success(request, 'Sistem berjaya ditambah!')
            return redirect(reverse_lazy('sistem_home'))
    else:
        form = SistemForm()
    return render(request, 'Pentadbir/daftar_peranan.html', {'form': form})

#reen tambah-----------------------------------------------------------------------------------------------------------

def SenaraiPeranan(request):
    a = RefPeranan.objects.all().order_by('Peranan')
    return render(request, 'Pentadbir/refperanan.html', {'peranan': a})

def Peranan_new(request):
    if request.method == "POST":
        request.POST = request.POST.copy()
        form = RefPerananForm(request.POST)

        if form.is_valid():
            peranan = form.save(commit=False)
            peranan.save()
            messages.success(request, 'Peranan berjaya ditambah!')
            return redirect(reverse_lazy('peranan_home'))
    else:
        form = RefPerananForm()
    return render(request, 'Pentadbir/daftar_peranan.html', {'form': form})

def Peranan_edit(request,pk):
    refperanan = get_object_or_404(RefPeranan, pk=pk)
    if request.method == "POST":
        form = RefPerananForm(request.POST, instance=refperanan)

        if form.is_valid():
            refperanan = form.save(commit=False)
            refperanan.save()
            messages.success(request, str(refperanan.Peranan) + " telah berjaya dikemaskini! ")
            return redirect(reverse_lazy('peranan_home'))

    else:
        form = RefPerananForm(instance=refperanan)
    return render(request, 'Pentadbir/edit_peranan.html', {'form': form})

def Peranan_delete(request,pk):

    refperanan = get_object_or_404(RefPeranan, pk=pk)
    if request.method == "POST":
        if request.POST.get("submit_yes", ""):
            per = refperanan.Peranan
            refperanan.delete()
            messages.success(request, "Peranan " + str(per) + " telah berjaya dihapuskan! ")
            return redirect(reverse_lazy('peranan_home'))

    # return render(request, 'Pentadbir/edit_peranan.html', {'form': form})
    return render(request, 'Pentadbir/peranan_confirm_delete.html', {'refperanan': refperanan, 'pk': pk})
# def DaftarPengguna(request):

#   # posts = []
#   # cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#   #                       "Server=10.101.1.100;"
#   #                       "Database=MCDB;"
#   #                       "uid=sa;pwd=cdbdev@2017")
#   # cursor = cnxn.cursor()
#   # # cursor.execute("SELECT ICNo,Nama,BUOrgChart,KategoriJawatan FROM TblPersonel where ICNo = '900131016875'")
#   # # cursor.execute("select ICNo,tp.nama, b.BUTitle as unit, c.BUTitle as bahagian, tp.KategoriJawatan from  MCDB.dbo.TblPersonel tp LEFT JOIN MCDB.dbo.TableBahagian b on REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),'')=REPLACE(REPLACE(b.BUOrgChart, Char(13),''),CHAR(10),'') LEFT JOIN MCDB.dbo.TableBahagian c on SUBSTRING(REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),''),1,7)+'0'= REPLACE(REPLACE(c.BUOrgChart,CHAR(13),''),CHAR(10),'') where tp.ICNo='890211025433'​")
#   # cursor.execute("select ICNo,tp.nama, b.BUTitle as unit, c.BUTitle as bahagian, tp.KategoriJawatan " \
#   #   "from  MCDB.dbo.TblPersonel tp LEFT JOIN MCDB.dbo.TableBahagian b on REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),'')," \
#   #   "CHAR(10),'')=REPLACE(REPLACE(b.BUOrgChart, Char(13),''),CHAR(10),'') LEFT JOIN MCDB.dbo.TableBahagian c on SUBSTRING(REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),''),1,7)+'0'= REPLACE(REPLACE(c.BUOrgChart,CHAR(13),''),CHAR(10),'')" \
#   #   " where tp.ICNo='890211025433'​")
#   # for obj in cursor.fetchall():
#   #   posts.append({"IC": obj[0], "Nama": obj[1], "Unit":obj[2], "Bahagian":obj[3], "KategoriJawatan":obj[4]})
#   # # context = {'all_posts':cursor.fetchall()}
#   # print(posts)
#   # for row in cursor:
#   #   print('row = %r' % (row,))
#   return render(request, 'Pentadbir/daftar_pengguna.html')

def Landing_page(request):
    return render(request, 'Pentadbir/landing_page.html')


def DaftarPengguna(request):
    if request.method == "POST":


        # form = DaftarPerananForm(request.POST)
        # print (form.cleaned_data['carian'])
        # nokp = form['carian'].value()

        addperanan = request.POST['submit']
        nokp = request.POST.get('carian', None)
        posts = []
        # cnxn = pyodbc.connect("Driver={SQL Server};"
        #                       "Server=10.101.1.100;"
        #                       "Database=MCDB;"
        #                       "uid=sa;pwd=cdbdev@2017")
        # cursor = cnxn.cursor()
        # sql = "select ICNo,tp.nama, b.BUTitle as unit, c.BUTitle as bahagian, tp.KategoriJawatan from  MCDB.dbo.TblPersonel tp LEFT JOIN MCDB.dbo.TableBahagian b on REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),'')=REPLACE(REPLACE(b.BUOrgChart, Char(13),''),CHAR(10),'') LEFT JOIN MCDB.dbo.TableBahagian c on SUBSTRING(REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),''),1,7)+'0'= REPLACE(REPLACE(c.BUOrgChart,CHAR(13),''),CHAR(10),'') where tp.ICNo='" + str(
        #     nokp) + "'"
        # cursor.execute(sql)
        # for obj in cursor.fetchall():
        #     posts.append({"IC": obj[0], "Nama": obj[1], "Unit": obj[2],
        #                   "Bahagian": obj[3], "KategoriJawatan": obj[4]})

        # if not posts:
        #     messages.error(request, 'Tiada Maklumat!')
        #     # print(posts)

        # Carian IC
        if nokp:

            print(request.POST)


            # perananpengguna = Peranan.objects.all()

            cnxn = pyodbc.connect("Driver={SQL Server};"
                                  "Server=10.101.1.100;"
                                  "Database=MCDB;"
                                  "uid=sa;pwd=cdbdev@2017")
            # cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.101.1.100;DATABASE=MCDB;UID=sa;PWD=cdbdev@2017')
            cursor = cnxn.cursor()
            sql = "select ICNo,tp.nama, b.BUTitle as unit, c.BUTitle as bahagian, tp.KategoriJawatan from  MCDB.dbo.TblPersonel tp LEFT JOIN MCDB.dbo.TableBahagian b on REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),'')=REPLACE(REPLACE(b.BUOrgChart, Char(13),''),CHAR(10),'') LEFT JOIN MCDB.dbo.TableBahagian c on SUBSTRING(REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),''),1,7)+'0'= REPLACE(REPLACE(c.BUOrgChart,CHAR(13),''),CHAR(10),'') where tp.ICNo='" + str(
                nokp) + "'"
            cursor.execute(sql)
            # row_count = cursor.execute("select ICNo,tp.nama, b.BUTitle as unit, c.BUTitle as bahagian, tp.KategoriJawatan from  MCDB.dbo.TblPersonel tp LEFT JOIN MCDB.dbo.TableBahagian b on REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),'')=REPLACE(REPLACE(b.BUOrgChart, Char(13),''),CHAR(10),'') LEFT JOIN MCDB.dbo.TableBahagian c on SUBSTRING(REPLACE(REPLACE(tp.BUOrgChart,CHAR(13),''),CHAR(10),''),1,7)+'0'= REPLACE(REPLACE(c.BUOrgChart,CHAR(13),''),CHAR(10),'') where tp.ICNo='"+str(nokp)+"'")
            # cursor.execute("select * from [MCDB].[dbo].[TblPersonel] where ICNo='"+str(nokp)+"'")
            # row = cursor.fetchall()

            # print (row)
            # context = {"row":row}

            # print (nokp)



            for obj in cursor.fetchall():
                posts.append({"IC": obj[0], "Nama": obj[1], "Unit": obj[2],
                              "Bahagian": obj[3], "KategoriJawatan": obj[4]})

            if not posts:
                messages.error(request, 'Tiada Maklumat!')
        else:
            icno = request.POST.get('icno',None)
            fPeranan = request.POST.get('peranan',None)
            print(icno,fPeranan)

            # for row in cursor:
            #   print('row = %r' % (row,))
            #   print('row = %r' % (row,))
    else:
        # form = DaftarPerananForm()
        posts = []
    perananpengguna = RefPeranan.objects.all()
    sistem = Sistem.objects.all()
    senaraiPerananpengguna = Peranan.objects.all()
    print(perananpengguna)
    # return render(request, 'Pentadbir/daftar_pengguna.html',{'form':form,'row':row})
    return render(request, 'Pentadbir/daftar_pengguna.html', {'posts': posts, 'perananpengguna':perananpengguna,'senaraiPerananpengguna':senaraiPerananpengguna,'sistem':sistem})

def TambahPeranan(request):
    pass