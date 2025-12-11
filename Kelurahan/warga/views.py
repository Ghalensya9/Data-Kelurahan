from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Warga, Pengaduan
from .forms import PengaduanForm, WargaForm

from rest_framework import viewsets, generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import WargaSerializer, PengaduanSerializer
from django_filters.rest_framework import DjangoFilterBackend


# ==== View berbasis template biasa ====

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
    template_name = 'warga/warga_form.html'
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


# ==== API berbasis DRF (generic views) ====

class WargaListAPIView(generics.ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer


# class WargaDetailAPIView(RetrieveAPIView):
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer


# ==== API berbasis ViewSet (untuk router /api/...) ====

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Removed DjangoFilterBackend to avoid missing template error
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']

class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'isi_pengaduan', 'status']     
    ordering_fields = ['tanggal_pengaduan', 'status']
    # Filter bawaan DRF (tanpa DjangoFilterBackend