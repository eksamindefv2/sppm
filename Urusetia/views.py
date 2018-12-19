from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Auditee
from .forms import AuditeeForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
import pyodbc
# Create your views here.


def SenaraiAuditee(request):
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

    a = Auditee.objects.all().order_by('SistemID')
    print(a)
    # return render(request,'Pentadbir/sistem.html',{ 'sistem': a,'posts':posts})
    return render(request, 'Urusetia/auditee.html', {'auditee': a})


def auditee_new(request):
    if request.method == "POST":
        request.POST = request.POST.copy()
        form = AuditeeForm(request.POST)

        if form.is_valid():
            auditee = form.save(commit=False)
            auditee.save()
            messages.success(request, 'Auditee berjaya ditambah!')
            return redirect(reverse_lazy('auditee_home'))
    else:
        form = AuditeeForm()
    return render(request, 'Urusetia/auditee_new.html', {'form': form})


def auditee_edit(request, pk):
    auditee = get_object_or_404(Auditee, pk=pk)
    if request.method == "POST":
        form = AuditeeForm(request.POST, instance=auditee)
        if form.is_valid():
            auditee = form.save(commit=False)
            auditee.createdby = request.user
            auditee.save()
            # return redirect('post_detail', pk=post.pk)
            # messages.success(request, "Student record with ID: " + str(student.pk) + " has been updated! ")
            return redirect(reverse_lazy('auditee_home'))
    else:
        form = AuditeeForm(instance=auditee)

    return render(request, 'Urusetia/auditee_edit.html', {'form': form})


def auditee_remove(request,pk):

    auditee = get_object_or_404(Auditee, pk=pk)
    if request.method == "POST":
        if request.POST.get("submit_yes", ""):
            auditee.delete()
            #  messages.success(request, "Student record with ID: " + str(icnum) + " has been removed! ")
            return redirect(reverse_lazy('auditee_home'))

    return render(request, 'Urusetia/auditee_confirm_remove.html', {'auditee': auditee, 'pk':pk})


class HomePageView(TemplateView):
    template_name = "index.html"
