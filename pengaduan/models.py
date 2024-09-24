from django.db import models
from django.contrib.auth.models import User

class Pengaduan(models.Model):
    JENIS_PENGADUAN = (
        ('bullying_perundungan', 'Bullying / Perundungan'),
        ('saran_kritik', 'Saran atau Kritik untuk Sekolah'),
        ('keluhan_lainnya', 'Keluhan Lainnya'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nama = models.CharField(max_length=255)
    nomor_whatsapp = models.CharField(max_length=15)
    peran = models.CharField(
        max_length=20,
        choices=(('siswa', 'Siswa'), ('guru', 'Guru'), ('wali_siswa', 'Wali Siswa')),
    )
    kelas = models.CharField(max_length=20, blank=True)
    anonim = models.BooleanField(default=False)
    jenis_pengaduan = models.CharField(max_length=50, choices=JENIS_PENGADUAN)
    deskripsi = models.TextField()
    bukti = models.FileField(upload_to='bukti/', blank=True)
    tanggal_pengaduan = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('menunggu', 'Menunggu Proses'),
        ('diproses', 'Sedang Diproses'),
        ('selesai', 'Selesai'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='menunggu')

    def __str__(self):
        return f"{self.nama} - {self.peran}"