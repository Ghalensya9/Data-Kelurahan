from django.urls import path
from .views import PengaduanDeleteView, PengaduanUpdateView, WargaListView, WargaDetailView, PengaduanListView, WargaCreateView, PengaduanCreateView,WargaUpdateView,WargaDeleteView

urlpatterns = [
    path('warga/', WargaListView.as_view(), name='warga_list'),
    path('warga/<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
    path('create/', WargaCreateView.as_view(), name='warga_create'),
    path('tambah/', PengaduanCreateView.as_view(), name='pengaduan_create'),
    path('<int:pk>/warga/edit/', WargaUpdateView.as_view(), name='warga_edit'),
    path('<int:pk>/warga/delete/', WargaDeleteView.as_view(), name='warga_delete'),
    path('<int:pk>/pengaduan/edit/', PengaduanUpdateView.as_view(), name='pengaduan_edit'),
    path('<int:pk>/pengaduan/delete/', PengaduanDeleteView.as_view(), name='pengaduan_delete')
]