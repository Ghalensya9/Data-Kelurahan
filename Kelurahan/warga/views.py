from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,UpdateView
from .models import Warga ,Pengaduan
from django.urls import reverse_lazy
from .forms import PengaduanForm, WargaForm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets # Impor viewsets
from .serializers import WargaSerializer, PengaduanSerializer
from .models import Warga
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly # Impor ini
from rest_framework.permissions import IsAdminUser 

class WargaListAPI(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer


class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga_list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan_list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' # Kita pakai template yang sama
    success_url = reverse_lazy('warga_list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga_list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan_list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan_list')

class WargaListAPIView(generics.ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

#class WargaDetailAPIView(RetrieveAPIView):
    #queryset = Warga.objects.all()
    #serializer_class = WargaSerializer

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer

# Tambahkan ViewSet untuk model Pengaduan
class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all()  # <--- Baris ini hilang di kode Anda
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser]

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Timpa izin default
