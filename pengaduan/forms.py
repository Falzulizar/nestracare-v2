from django import forms
from .models import Pengaduan

class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = [
            'nama', 'nomor_whatsapp', 'peran', 'kelas', 'anonim',
            'jenis_pengaduan', 'deskripsi', 'bukti'
        ]
        widgets = {
            'deskripsi': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kelas'].required = False