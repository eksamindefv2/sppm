from django.shortcuts import render
from .models import TblSistem
from .forms import TblSistemForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

# Create your views here.
def SenaraiSistem(request):
    # List of records
    a = TblSistem.objects.all().order_by('NamaSistem')
    print(a)
    return render(request,'Persediaan/sistem.html',{ 'sistem': a })


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
	return render(request, 'persediaan/sistem_new.html', {'form': form})