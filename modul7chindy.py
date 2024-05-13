print(" "*6,"JADWAL HARIAN CHINDY AULIA RAHMI ")
print("-"*45)
print()
print("Selamat datang chindy!!")

jadwal_kegiatan = []
def menambahkan():
    waktu_mulai = input("Waktu mulai kegiatan (__:__)      : ")
    waktu_selesai = input("Waktu selesainya kegiatan (__:__) : ")
    deskripsi_kegiatan = input("Nama deskripsi kegiatan ini ? : ")
    jadwal_kegiatan.append([waktu_mulai, waktu_selesai, deskripsi_kegiatan])
    print("Kegiatan '{}' yang anda masukkan telah berhasil ditambahkan. ". format(deskripsi_kegiatan))

def menghapus():
    hapus = input("Masukkan deskripsi kegiatan yang ingin dihapus: ")
    for kegiatan in jadwal_kegiatan:
        if kegiatan [2] == hapus:
            jadwal_kegiatan.remove(kegiatan)
            print("Kegiatan '{}' berhasil dihapus dari jadwal.".format(hapus))
            return jadwal_kegiatan
    print("Kegiatan '{}' tidak ditemukan dalam jadwal.".format(hapus))
    return jadwal_kegiatan
    
def menampilkan():
    if not jadwal_kegiatan:
        print("Belum ada kegiatan yang anda tambahkan.")
    else:
        print("Jadwal kegiatan:")
        print("-"*40)
        print("| {:<4} | {:<20} | {:<14} | {:<14} |".format("NO.","Jadwal","Deskripsi","Waktu mulai","Waktu Selesai"))
        for i in range (len(jadwal_kegiatan)):
            kegiatan = jadwal_kegiatan[i]
            print("| {:<4} | {:<20} | {:<14} | {:<14} |".format(i+1, kegiatan[2],kegiatan[0],kegiatan[1]))
        return jadwal_kegiatan


while True:
        print ()
        print ("    Menu tampilan : ")
        print (" 1. Menambahkan kegiatan anda ")
        print (" 2. Menghapus kegiatan anda ")
        print (" 3. Menampilkan jadwal ")
        print(" 4. Keluar")

        menu = int(input("Silahkan masukan menu pilihan anda : "))
        if menu == 1 :
          menambahkan()
        elif menu == 2 :
            menghapus()
        elif menu == 3 :
            menampilkan()
        else :
         print("Anda telah keluar dari program ! semangat!")
         break
