from django.urls import path
from .views import WargaListView,WargaDetailView,PengaduanListView

urlpatterns = [
    path('warga/', WargaListView.as_view(), name='warga-list'),
    path('warga/<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list')
]