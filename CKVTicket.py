from termcolor import colored, cprint
import os 
import time

os.system("cls")
#Fungsi untuk menampilkan logo awal 
def logo():
  for i in range (12):                      #mencetak background sebelum tulisan ckv
    cprint("  "*68, "white","on_cyan")

  ckv = [                                        #mencetak tulisan ckv
   "||||||||   ||||||||||||||       ||| ",
   "|||   ||              |||      |||  ",
   "|||        |||   ||   |||     |||   ",
   "|||        |||  ||    |||    |||    ",
   "|||        |||||      |||   |||     ",
   "|||   ||   |||  ||    |||  |||      ",
   "||||||||   |||   ||   ||||||        "                              
   ]
  for line in ckv :
    posisi_kata = line.center(136)
    for char in posisi_kata :
      if char != " ":
        cprint (" ", "white", "on_white",end="")
      else :
        cprint (" ", "cyan", "on_cyan", end="")
    print()

  cprint("  "*68, "white","on_cyan")                 #mencetak tampilan tulisan ticket
  cprint(" "*72, "white","on_cyan",end="")
  cprint("t i c k e t","white","on_magenta",end="")
  cprint(" "*53, "white","on_cyan")
  for i in range (13):                               #mencetak background setelah tulisan ticket 
   cprint("  "*68, "white","on_cyan")

def welcome():
  for i in range (16):                                       #mencetak background
    cprint("  "*68, "white","on_cyan")

  cprint(" "*54, "white", "on_cyan",end="")                  #mencetak tulisan selamat datang
  cprint("[S E L A M A T   D A T A N G]","white","on_cyan",end="")
  cprint(" "*53, "white", "on_cyan")

  for i in range (16):                                       #mencetak background
    cprint("  "*68, "white","on_cyan")

def film():
  cprint(" "*136,"white","on_cyan")
  cprint(" "*63, "white", "on_cyan",end="")
  cprint("CKV ticket","black","on_cyan",end="")
  cprint(" "*63, "white", "on_cyan")
  cprint("  "*68, "white", "on_cyan") 
  cprint(" "*5, "white", "on_cyan",end=" "*126)
  cprint(" "*5, "white", "on_cyan")

  latar = [
    "                                                                                                                          ",
    "                                                                                                                          ",
    "            |||                             ||||||||||||||||||                     |||||||||||||||||||                    ",
    "           |||||                            ||||||||||||||||||                     |||||||||||||||||||                    ",
    "         |||| |||                                       ||||||                                  ||||||                    ",
    "       ||||   ||||                                      ||||||                                  ||||||                    ",
    "              ||||                                      ||||||                                  ||||||                    ",
    "              ||||                          ||||||||||||||||||                     |||||||||||||||||||                    ",
    "              ||||                          ||||||                                              ||||||                    ",
    "              ||||                          ||||||                                              ||||||                    ",
    "              ||||                          ||||||                                              ||||||                    ",
    "              ||||                          ||||||||||||||||||                     |||||||||||||||||||                    ",
    "        ||||||||||||||                      ||||||||||||||||||                     |||||||||||||||||||                    ",
    "                                                                                                                          ",
    "                                                                                                                          "
    ]
  
  for line in latar:
    cprint(" " * 5, "white", "on_cyan", end="")         #mencetak bagian margin kiri
    print(" " * 10, end="")
    
    panjang_karakter = 121  
    posisi_kata = line.center(panjang_karakter)
    
    pict1 = posisi_kata[0:31]                           #mencetak nomor 1
    for char in pict1:
      if char != " ":
       cprint(" ", "white", "on_white", end="")
      else:
        cprint(" ", "white", "on_light_red", end="")
    
    print(" " * 5, end="")                              #jarak antara nomor 1 dan 2
    
    pict2 = posisi_kata[38:70]                          #mencetak nomor 2
    for char in pict2:
      if char != " ":
        cprint(" ", "white", "on_white", end="")
      else:
        cprint(" ", "white", "on_light_green", end="")
    
    print(" " * 5, end="")                              #jarak antara nomor 2 dan 3
    
    pict3 = posisi_kata[77:109]                         #mencetak nomor 3
    for char in pict3:
      if char != " ":
        cprint(" ", "white", "on_white", end="")
      else:
        cprint(" ", "white", "on_light_yellow", end="")
    
    print(" " * 11, end="")                            #jarak antara margin kanan dengan nomor 3
    
    cprint(" " * 5, "white", "on_cyan", end="")        #mencetak margin sebelah kanan
    print()                                            # Pindah ke baris berikutnya setelah selesai mencetak satu baris

  for i in range(2):                                   #mencetak margin kiri kanan dua baris ke bawah
   cprint(" "*5, "white", "on_cyan",end=" "*126)
   cprint(" "*5, "white", "on_cyan")
   
  film_1 = [
    ["  HOW TO MAKE MILLIONS BEFORE  ","      VINA: SEBELUM 7 HARI      ","  HAIKYU!! THE DUMPSTER BATTLE  "],
    ["        GRANDMA  DIES          ","                                ","                                "],
    ["Genre       : Family Film/Drama"," Genre       : Horor/Drama      "," Genre       : Komedi/Animasi   "],
    ["Sutradara   : Pat Boonnitipat  "," Sutradara   : Anggy Umbara     "," Sutradara   : Susumu Mitsunaka "],
    ["Bahasa      : Thailand         "," Bahasa      : Indonesia        "," Bahasa      : Jepang           "],
    ["Umur        : SU               "," Umur        : 17+              "," Umur        : SU               "],
    ["Harga Tiket : Rp 50.000        "," Harga Tiket : Rp 50.000        "," Harga Tiket : Rp 50.000        "]
  ] 
   
  for i in range (6):
    cprint(" "*5, "white", "on_cyan",end=" "*10)
    cprint(film_1[i][0],"black","on_white",end=" "*5)
    cprint(film_1[i][1],"black","on_white",end=" "*5)
    cprint(film_1[i][2],"black","on_white",end=" "*11)
    cprint(" "*5,"white","on_cyan")

  cprint(" "*5, "white", "on_cyan",end=" "*126) 
  cprint(" "*5, "white", "on_cyan")

  cprint(" "*136,"white","on_cyan")

def keterangan():
  print("JADWAL FILM",end=" "*58)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*126,end="")
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*30)
  cprint("10.30 WIB", "white","on_light_green",end=" "*10)
  cprint("13.00 WIB", "white","on_light_green",end=" "*10)
  cprint("15.40 WIB", "white","on_light_green",end=" "*10)
  cprint("20.00 WIB", "white","on_light_green",end=" "*30)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*126,end="")
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*60)
  print("NO SEAT",end=" "*59)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*126,end="")
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*40,end="")
  cprint(" "*47,"white","on_light_grey",end=" "*39)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*40,end="")
  for i in range (1,6):
    cprint("  ","white","on_light_grey",end="   ")
    print(i,end="   ")
  cprint("  ","white","on_light_grey",end=" "*39)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*40,end="")
  for i in range (6,11):
    cprint("  ","white","on_light_grey",end="   ")
    print( "{:<4}" .format(i)  ,end="")
  cprint("  ","white","on_light_grey",end=" "*39)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*40,end="")
  for i in range (11,16):
    cprint("  ","white","on_light_grey",end="   ")
    print( "{:<4}" .format(i)  ,end="")
  cprint("  ","white","on_light_grey",end=" "*39)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*40,end="")
  cprint(" "*47,"white","on_light_grey",end=" "*39)
  cprint(" "*5,"white","on_cyan")

  for i in range(5):
   cprint(" "*5,"white","on_cyan",end="")
   print(" "*126,end="")
   cprint(" "*5,"white","on_cyan")
  cprint(" "*136,"white","on_cyan")
  cprint(" "*136,"white","on_cyan")

def cetak():
 print(" "*40,end="")
 cprint(" "*56, "white","on_magenta")
 print(" "*40,end="")
 cprint(" "*23,"white","on_magenta",end="")
 cprint("CKV TICKET","white","on_magenta",end="")
 cprint(" "*23,"white","on_magenta")
 print(" "*40,end="")
 cprint(" "*56, "white","on_magenta")
 print(" "*40,end="")
 cprint( "FILM   : {:<47}" .format(pesan['judul']),"white","on_magenta")
 print(" "*40,end="")
 cprint( "JADWAL : {:<47}" .format(jadwal),"white","on_magenta")
 print(" "*40,end="")
 cprint( "SEAT   : {:<47}" .format(seat),"white","on_magenta")
 print(" "*40,end="")
 cprint( "HARGA  : {:<47}" .format(pesan['harga']),"white","on_magenta")
 print(" "*40,end="")
 cprint(" "*56, "white","on_magenta")
 print(" "*40,end="")
 cprint(" "*22,"white","on_magenta",end="")
 cprint("TERIMA KASIH","white","on_magenta",end="")
 cprint(" "*22,"white","on_magenta")
 print(" "*40,end="")
 cprint(" "*56, "white","on_magenta")
   
logo()
time.sleep(3)
os.system("cls")

welcome()
time.sleep(1)
os.system("cls")

film()
print()
print(" "*50,end="")
pilih = int(input("Masukkan Film Pilihan Anda : "))


if pilih == 1 :
  time.sleep(1)
  os.system("cls")
  cprint(" "*136,"white","on_cyan")
  cprint(" "*136,"white","on_cyan")

  for i in range (2):
    cprint(" "*5,"white","on_cyan",end="")
    print(" "*126,end="")
    cprint(" "*5,"white","on_cyan")

  cprint(" "*5,"white","on_cyan",end=" ")
  print(" "*42,end="")
  cprint("HOW TO MAKE MILLIONS BEFORE GRANDMA DIES","white","on_light_magenta",end="")
  print(" "*43,end="")
  cprint(" "*5,"white","on_cyan")

  for i in range (2):
    cprint(" "*5,"white","on_cyan",end="")
    print(" "*126,end="")
    cprint(" "*5,"white","on_cyan")

  cprint(" "*5,"white","on_cyan",end=" "*59)
  print("SINOPSIS",end=" "*59)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*17)
  cprint(" Seorang pria berhenti bekerja untuk merawat neneknya yang sedang sekarat, termotivasi oleh ","white","on_light_red",end=" "*17)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*17)
  cprint("  kekayaannya. Dia merencanakan untuk memenangkan hati neneknya sebelum neneknya meninggal. ","white","on_light_red",end=" "*17)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*126,end="")
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*57)

  keterangan()

  print()
  print(" "*53,end=" ")
  jadwal = input("Pilih Jadwal Film : ")
  print()
  print(" "*53,end=" ")
  seat = input("Pilih Nomor Seat : ")

  pesan = {
    "jadwal": jadwal,
    "seat"  : seat,
    "judul" : "HOW TO MAKE MILLIONS BEFORE GRANDMA DIES",
    "harga" : "Rp 50.000,00"
  }

  with open ("ckv.txt","a") as file:
    file.write(f"{pesan['judul']:<42}|  {pesan['jadwal']:<10}| {pesan['seat']:<10} |  {pesan['harga']:<10}|\n")

  time.sleep(1)
  os.system("cls")

  cetak()

elif pilih == 2 :
  time.sleep(1)
  os.system("cls")
  cprint(" "*136,"white","on_cyan")
  cprint(" "*136,"white","on_cyan")

  for i in range (2):
    cprint(" "*5,"white","on_cyan",end="")
    print(" "*126,end="")
    cprint(" "*5,"white","on_cyan")

  cprint(" "*5,"white","on_cyan",end=" ")
  print(" "*53,end="")
  cprint("VINA: SEBELUM 7 HARI","white","on_light_magenta",end="")
  print(" "*52,end="")
  cprint(" "*5,"white","on_cyan")

  for i in range (2):
    cprint(" "*5,"white","on_cyan",end="")
    print(" "*126,end="")
    cprint(" "*5,"white","on_cyan")

  cprint(" "*5,"white","on_cyan",end=" "*59)
  print("SINOPSIS",end=" "*59)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*17)
  cprint(" Jenazah Almarhumah Vina mengalami kecelakaan motor tunggal. Vina merasuki tubuh sahabatnya ","white","on_light_red",end=" "*17)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*17)
  cprint("      Ia hanya punya waktu sebelum 7 hari untuk mengungkap kebenaran yang menyakitkan.      ","white","on_light_red",end=" "*17)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*126,end="") 
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*57)

  keterangan()
  
  print()
  print(" "*53,end=" ")
  jadwal = input("Pilih Jadwal Film : ")
  print()
  print(" "*53,end=" ")
  seat = input("Pilih Nomor Seat : ")

  pesan = {
    "jadwal": jadwal,
    "seat"  : seat,
    "judul" : "VINA: SEBELUM 7 HARI",
    "harga" : "Rp 50.000,00"
  }

  with open ("ckv.txt","a") as file:
    file.write(f"{pesan['judul']:<42}|  {pesan['jadwal']:<10}| {pesan['seat']:<10} |  {pesan['harga']:<10}|\n")

  time.sleep(1)
  os.system("cls")

  cetak()
  
elif pilih == 3 :
  time.sleep(1)
  os.system("cls")
  cprint(" "*136,"white","on_cyan")
  cprint(" "*136,"white","on_cyan")
  
  for i in range (2):
    cprint(" "*5,"white","on_cyan",end="")
    print(" "*126,end="")
    cprint(" "*5,"white","on_cyan")

  cprint(" "*5,"white","on_cyan",end=" ")
  print(" "*49,end="")
  cprint("HAIKYU!! THE DUMPSTER BATTLE","white","on_light_magenta",end="")
  print(" "*48,end="")
  cprint(" "*5,"white","on_cyan")

  for i in range (2):
    cprint(" "*5,"white","on_cyan",end="")
    print(" "*126,end="")
    cprint(" "*5,"white","on_cyan")

  cprint(" "*5,"white","on_cyan",end=" "*59)
  print("SINOPSIS",end=" "*59)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*17)
  cprint("SMA Karasuno meraih kemenangan atas SMA Inarizaki di putaran kedua turnamen SMA Musim Semi. ","white","on_light_red",end=" "*17)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*17)
  cprint("                Kini, mereka bersiap menghadapi rival lama mereka, SMA Nekoma               ","white","on_light_red",end=" "*17)
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end="")
  print(" "*126,end="")
  cprint(" "*5,"white","on_cyan")
  cprint(" "*5,"white","on_cyan",end=" "*57)

  keterangan()

  print()
  print(" "*53,end=" ")
  jadwal = input("Pilih Jadwal Film : ")
  print()
  print(" "*53,end=" ")
  seat = input("Pilih Nomor Seat : ")
  
  pesan = {
    "jadwal": jadwal,
    "seat"  : seat,
    "judul" : "HAIKYU!! THE DUMPSTER BATTLE",
    "harga" : "Rp 50.000,00"
  }

  with open ("ckv.txt","a") as file:
    file.write(f"{pesan['judul']:<42}|  {pesan['jadwal']:<10}| {pesan['seat']:<10} |  {pesan['harga']:<10}|\n")

  time.sleep(1)
  os.system("cls")

  cetak()

else:
 os.system("cls")
 print(end=" "*50)
 cprint("Pilihan Anda Tidak Valid","black","on_red")
 print(end=" "*50)
 cprint(" Silahkan Ulang Kembali ","black","on_red")
  

