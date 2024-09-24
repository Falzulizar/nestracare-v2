from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from django.shortcuts import redirect
from django.contrib import messages
from .models import Pengaduan

admin.site.site_header = 'Nestracare - Admin'
admin.autodiscover()
admin.site.enable_nav_sidebar = False 

@admin.register(Pengaduan)
class PengaduanAdmin(admin.ModelAdmin):
    list_display = ('get_nama', 'tanggal_pengaduan', 'jenis_pengaduan', 'status_pengaduan', 'peran')
    list_filter = ('jenis_pengaduan', 'tanggal_pengaduan', 'peran')
    search_fields = ('nama', 'nomor_whatsapp', 'deskripsi')
    readonly_fields = ('tanggal_pengaduan', 'user', 'get_nama', 'nomor_whatsapp', 'peran', 'kelas', 'anonim', 'jenis_pengaduan', 'deskripsi', 'bukti', 'action_buttons') 

    def status_pengaduan(self, obj):
        if obj.status == 'selesai':
            return "Selesai"
        elif obj.status == 'diproses':
            return "Sedang Diproses"
        else:
            return "Menunggu Proses"
    status_pengaduan.short_description = 'Status'

    def proses_pengaduan(self, request, pk):
        pengaduan = Pengaduan.objects.get(pk=pk)
        pengaduan.status = 'diproses'  # Ubah status menjadi 'diproses'
        pengaduan.save()
        messages.success(request, f'Pengaduan {pengaduan.id} sedang diproses.')
        return redirect('admin:pengaduan_pengaduan_changelist')

    def selesai_pengaduan(self, request, pk):
        pengaduan = Pengaduan.objects.get(pk=pk)
        pengaduan.status = 'selesai'  # Ubah status menjadi 'selesai'
        pengaduan.save()
        messages.success(request, f'Pengaduan {pengaduan.id} telah diselesaikan.')
        return redirect('admin:pengaduan_pengaduan_changelist')

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<int:pk>/proses/', self.admin_site.admin_view(self.proses_pengaduan), name='pengaduan_pengaduan_proses'),
            path('<int:pk>/selesai/', self.admin_site.admin_view(self.selesai_pengaduan), name='pengaduan_pengaduan_selesai'),
        ]
        return my_urls + urls

    def action_buttons(self, obj):
        return format_html(
            '<a class="button" href="{}">Proses</a> '
            '<a class="button" href="{}">Selesai</a>',
            reverse('admin:pengaduan_pengaduan_proses', args=[obj.pk]),
            reverse('admin:pengaduan_pengaduan_selesai', args=[obj.pk]),
        )
    action_buttons.short_description = 'Aksi'
    action_buttons.allow_tags = True

    def get_nama(self, obj):
        request = getattr(self, 'request', None)
        if obj.anonim and request and not request.user.is_superuser:
            return "Anonim"
        return obj.nama
    get_nama.short_description = 'Nama'
    get_nama.admin_order_field = 'nama'

    def get_queryset(self, request):
        self.request = request 
        qs = super().get_queryset(request)
        return qs