from django.shortcuts import render
from .models import Sesi
from .forms import SesiForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
import pyodbc
from django.http import JsonResponse
from django.template.loader import render_to_string


#Senarai Sesi
def SenaraiSesi(request):
    a = Sesi.objects.all().order_by('Siri')
    total = sum([i.Status for i in a])
    print(a)
    # return render(request,'Pentadbir/sistem.html',{ 'sistem': a,'posts':posts})
    return render(request, 'Urusetia/sesi.html', {'sesi': a, 'total': total})

#Tambah Sesi
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

#Edit Sesi
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


################ Django CRUD modal form #####################################################

# Senarai semua sistem
def sesi_list(request):
    a = Sesi.objects.all().order_by('Siri')

    total = sum([i.Status for i in a])
    print(a)
    # return render(request,'Pentadbir/sistem.html',{ 'sistem': a,'posts':posts})
    return render(request, 'Urusetia/sesi_list.html', {'sesi': a, 'total': total})

# Simpan Form Generic
def save_sesi_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


# Cipta Sesi
def sesi_create(request):
    if request.method == 'POST':
        form = SesiForm(request.POST)
        msg = 'Sesi' + request.POST.get('Siri', None) + ' telah berjaya ditambah!'
        messages.success(request, msg)
    else:
        form = SesiForm()
    return save_sesi_form(request, form, 'Urusetia/partial_sesi_create.html')

# Update Sistem
def sesi_update(request, pk):
    sesi = get_object_or_404(Sesi, pk=pk)
    if request.method == 'POST':
        form = SesiForm(request.POST, instance=sesi)
        msg = 'Sesi ' + request.POST.get('Siri', None)  +' telah berjaya dikemaskini!'
        messages.success(request, msg)
    else:
        form = SesiForm(instance=sesi)
    return save_sesi_form(request, form, 'Urusetia/partial_sesi_update.html')
