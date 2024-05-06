print()
print("***SELAMAT DATANG DI MASKAPAI MUDA-MUDI***")
print("   ------------------------------------   ")
print()
print("Berikut adalah jadwal penerbangan yang tersedia : ")
print("     [tekan enter untuk menampilkan]          ")
input()

nomor = [1,2,3,4]
tabel= [
    ['Padang', 'Jakarta', 'Medan','Semarang'],
    ['Jakarta', 'Pekanbaru', 'Yogyakarta','Karimunjawa'],
    ['15.00','12.00','06.00','11.00'],
    ['16.50','13.40','10.50','11.40']
]

print("-"*89)
print("|  {:<12}  |{:<12}  | {:<12} | {:<12} | {:<12} |".format("NO","Kota Asal", "Kota Tujuan",
                                                                "Waktu Keberangkatan","Waktu Kedatangan"))
print("-"*89)
for i in range(4):
    print("|  {:<12}  |{:<12}  | {:<12} | {:<19} | {:<16} |".format(nomor[i],tabel[0][i], tabel[1][i], tabel[2][i],tabel[3][i]))
print("-"*89)

print("")
print("Untuk menentukan rute tercepat diantara jadwal penerbangan yang tersedia, \nSilahkan masukkan kode jadwal penerbangan yang tersedia sesuai dengan nomor tabel :")

jadwal_1 = int(input('Jadwal penerbangan pertama(1-4) : '))
jadwal_2 = int(input("Jadwal penerbangan ke-dua (1-4) : "))
print()

if (((jadwal_1 == 1) and (jadwal_2 == 2))) or ((jadwal_1 == 2) and (jadwal_2 == 1)) :
    print ("Rute tercepat diantara ", tabel[0][0], "-",tabel[1][0], "dan", tabel[0][1], "-",tabel[1][1], "adalah : rute", tabel[0][0], "-",tabel[1][0], "\ndengan lama perjalanan selama 110 menit" )

elif ((jadwal_1 == 1 and (jadwal_2 == 3))) or ((jadwal_1 == 3) and (jadwal_2 == 1)) :
    print ("Rute tercepat diantara ", tabel[0][0], "-",tabel[1][0], "dan", tabel[0][2], "-",tabel[1][2], "adalah : rute", tabel[0][2], "-",tabel[1][2], "\ndengan lama perjalanan selama 290 menit" )

elif ((jadwal_1 == 1 and (jadwal_2 == 4))) or ((jadwal_1 == 4) and (jadwal_2 == 1)) :
    print ("Rute tercepat diantara ", tabel[0][0], "-",tabel[1][0], "dan", tabel[0][3], "-",tabel[1][3], "adalah : rute", tabel[0][0], "-",tabel[1][0], "\ndengan lama perjalanan selama 110 menit" )

elif ((jadwal_1 == 2 and (jadwal_2 == 3))) or ((jadwal_1 == 3) and (jadwal_2 == 2)) :
    print ("Rute tercepat diantara ", tabel[0][1], "-",tabel[1][1], "dan", tabel[0][2], "-",tabel[1][2], "adalah : rute", tabel[0][2], "-",tabel[1][2], "\ndengan lama perjalanan selama 290 menit" )

elif ((jadwal_1 == 2 and (jadwal_2 == 4))) or ((jadwal_1 == 4) and (jadwal_2 == 2)) :
    print ("Rute tercepat diantara ", tabel[0][1], "-",tabel[1][1], "dan", tabel[0][3], "-",tabel[1][3], "adalah : rute", tabel[0][1], "-",tabel[1][1], "\ndengan lama perjalanan selama 100 menit" )

elif ((jadwal_1 == 3 and (jadwal_2 == 4))) or ((jadwal_1 == 4) and (jadwal_2 == 3)) :
    print ("Rute tercepat diantara ", tabel[0][2], "-",tabel[1][2], "dan", tabel[0][3], "-",tabel[1][3], "adalah : rute", tabel[0][2], "-",tabel[1][2], "\ndengan lama perjalanan selama 290 menit" )

elif (jadwal_1 > 4 or jadwal_2 > 4) :
 print("Kode Anda Tidak Valid")

print("\n[Terima kasih telah menggunakan program maskapai kami ! ]")