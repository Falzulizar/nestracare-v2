# Generated by Django 5.0.3 on 2024-09-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengaduan', '0003_pengaduan_nomor_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengaduan',
            name='status',
            field=models.CharField(choices=[('menunggu', 'Menunggu Proses'), ('diproses', 'Sedang Diproses'), ('selesai', 'Selesai')], default='menunggu', max_length=10),
        ),
    ]
