from django.contrib import admin
from django.urls import path
from pengaduan.views import pengaduan_view, sukses, index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('pengaduan/', pengaduan_view, name='pengaduan'),
    path('pengaduan/sukses/', sukses, name='sukses'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)