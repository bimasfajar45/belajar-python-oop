# Sistem Data Mahasiswa

"""
Membuat sistem input mahasiswa dengan menggunakan class sederhana

yang berisi beberapa method
1. tampilkan data
2. update ipk
3. Status kelulusan
"""

class Mahasiswa:
    # buat insesnya dengan (nama, nim, jurusan, ipk)
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    # Buat method dengan untuk menampilkan data mahasiswa hasil 
    def menampilkan_data(self): # beri self di tanda kurung agar sistem mendeteksi bahwa baris ini ter integrasi dengan class
        print(f"Nama : {self.nama}")
        print(f"NIM : {self.nim}")
        print(f"IPK : {self.ipk}")

    # method untuk mengupdate ipk
    def update_ipk(self, ipk_update):
        self.ipk = ipk_update

    # cek apakah memenuhi kriteria untuk lulus
    def cek_kelulusan(self):
        if self.ipk >= 2.8:
            print(f"IPK = {self.ipk} LULUS ✅")
        else:
            print(f"IPK = {self.ipk} TIDAK LULUS ❌")

# Buat intens dan panggil atributnya
mhs_1 = Mahasiswa("Bimas Fajar Fatihudhin", 25552020023, 2.3)
mhs_1.menampilkan_data()
mhs_1.cek_kelulusan()
