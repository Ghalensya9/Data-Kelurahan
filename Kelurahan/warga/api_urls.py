# warga/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

# Buat sebuah router dan daftarkan ViewSet kita
router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')

# URL API sekarang ditentukan secara otomatis oleh router.
urlpatterns = [
    path('', include(router.urls)),
]

# router.register(r'warga', ...): Mendaftarkan WargaViewSet ke router dengan prefix URL warga.
# router.register(r'pengaduan', ...): Mendaftarkan PengaduanViewSet ke router dengan prefix URL pengaduan.