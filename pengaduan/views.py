from django.shortcuts import render, redirect
from .forms import PengaduanForm

def index(request):
    return render(request, 'pengaduan/index.html')


def pengaduan_view(request):
    if request.method == 'POST':
        form = PengaduanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sukses') 
    else:
        form = PengaduanForm()
    return render(request, 'pengaduan/pengaduan.html', {'form': form})

def sukses(request):
    return render(request, 'pengaduan/sukses.html')

