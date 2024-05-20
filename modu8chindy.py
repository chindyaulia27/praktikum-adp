print("       [ Data Pasien Dr. Chindy Rahmi ]       ")
print("-"*49)

def data(pasien):
    with open("datapasien.txt","a") as file:
        file.write(f"{pasien['nama']:<24}| {pasien['umur']:<5} | {pasien['gender']:<13} | {pasien['goldar']:<14} | {pasien['penyakit']:<16} | {pasien['obat']:<10} "f"\n")
    print("Data telah berhasil ditambahkan ! ")

def hapus(nama) :
    with open ("datapasien.txt","r") as file:
     lines = file.readlines() 
    with open ("datapasien.txt","w") as file:
        for line in lines:
            if line.split("|")[0] .strip() != nama : 
                file.write(line)

def tampil():
    with open ("datapasien.txt") as file :
        for line in file:
            print(line)

while True: 
   print()
   print("Halo! Berikut beberapa pilihan yang dapat anda pilih ! ")
   print("1. Menambahkan data pasien")
   print("2. Menghapus data pasien ")
   print("3. Menampilkan data pasien ")
   print("4. Keluar ")

   pilih = int(input("Silahkan masukkan pilihan anda : "))

   if pilih == 1 :
     print()
     print("Silahkan isi data berikut dengan benar !")
     pasien = {
         "nama" : input("Nama                : "),
         "umur" : input("Umur                : "),
         "gender" : input("Jenis kelamin (L/P) : "),
         "goldar" : input("Golongan darah      : "),
         "penyakit" : input("Riwayat penyakit    : "),
         "obat" : input("Daftar obat         : ")
     }
     data(pasien)

   elif pilih == 2 :
      print()
      nama = input("Nama pasien yang ingin anda hapus : ")
      hapus(nama)
      print("Berhasil dihapus!")
    
   elif pilih == 3 :
       print("Daftar pasien anda : ")
       print("{:<23} | {:<5} | {:<6} | {:<8} | {:<15} | {:<10} ".format("Nama","Umur","Jenis Kelamin","Golongan Darah","Riwayat Penyakit","Obat"))
       tampil()

   elif pilih == 4 :
       print()
       print("[ Anda telah keluar dari program ]")
       break
   
   else:
       print()
       print("[ Kode yang anda masukkan tidak sesuai, silahkan coba lagi ]")