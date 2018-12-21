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

#################################################################################################
#   VIEWS FOR AUDITEE
#################################################################################################

def SenaraiAuditee(request):

    a = Auditee.objects.all().order_by('SistemID')
    print(a)

    #a.SubAuditee.AuditeeID

    return render(request, 'Urusetia/auditee.html', {'auditee': a})


def auditee_detail(request,pk):
    a = get_object_or_404(Auditee, pk=pk)
    print(a)
    #print(student.name)
    return render(request, 'Urusetia/auditee_detail.html', {'a': a})


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
            messages.success(request, "Maklumat auditee " + str(auditee.NamaAuditee) + " telah dikemaskini! ")
            return redirect(reverse_lazy('auditee_home'))
    else:
        form = AuditeeForm(instance=auditee)

    return render(request, 'Urusetia/auditee_edit.html', {'form': form})


def auditee_remove(request,pk):

    auditee = get_object_or_404(Auditee, pk=pk)
    if request.method == "POST":
        if request.POST.get("submit_yes", ""):
            auditee.delete()
            messages.success(request, "Maklumat Auditee " + str(icnum) + " has been removed! ")
            return redirect(reverse_lazy('auditee_home'))

    return render(request, 'Urusetia/auditee_confirm_remove.html', {'auditee': auditee, 'pk':pk})


#################################################################################################
# VIEWS FOR SUBAUDITEE
#################################################################################################

class HomePageView(TemplateView):
    template_name = "index.html"


