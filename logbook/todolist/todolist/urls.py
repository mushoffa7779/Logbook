
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('task/', include('task.urls')),
    path('peminjam/', include('peminjam.urls')),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('mitra/', include('mitra.urls')),
    path('profil/', include('profil.urls')),
    path('accounts/',include("accounts.urls")),

]
