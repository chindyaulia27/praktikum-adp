program Pesanan_Menu;
uses crt;
const
 A = 10000;   F = 5000;   K = 13000 ;
 B = 8000;    G = 7000;   L = 12000;
 C = 8000;    H = 7000;   M = 18000;
 D = 15000;   I = 7000;
 E = 10000;   J = 4000;
var
 nomor, pesanan, jumlah, harga :Longint;


begin

clrscr;
gotoXY(45,1); writeln(' -----------------------------------------');
gotoXY(45,2); writeln('| SELAMAT DATANG DI RESTORAN BUNDA GRANDE |');
gotoXY(45,3); writeln(' -----------------------------------------');
gotoXY(42,4); writeln('Berikut beberapa opsi menu yang dapat ditampilkan : ');
gotoXY(45,5); writeln(' 1. Makanan ');
gotoXY(45,6); writeln(' 2. Minuman ');
gotoXY(45,7); writeln(' 3. Makanan dan Minuman');
gotoXY(32,9); write  ('Silahkan masukkan kode nomor yang sesuai agar menu dapat ditampilkan : ');readln(nomor);

if (nomor = 1) then
  begin
   gotoXY(32,11); writeln('--------------------------------------------------------------------------');
   gotoXY(50,12); writeln('            MENU MAKANAN              ');
   gotoXY(50,13); writeln(' ____________________________________ ');
   gotoXY(50,14); writeln('| NO |      Makanan     |   Harga    |');
   gotoXY(50,15); writeln('|____|__________________|____________|');
   gotoXY(50,16); writeln('| 1. | Nasi Goreng      | Rp. 10.000 |');
   gotoXY(50,17); writeln('| 2. | Mie Goreng       | Rp. 8.000  |');
   gotoXY(50,18); writeln('| 3. | Bihun Goreng     | Rp. 8.000  |');
   gotoXY(50,19); writeln('| 4. | Soto Daging      | Rp. 15.000 |');
   gotoXY(50,20); writeln('| 5. | Bubur Ayam       | Rp. 10.000 |');
   gotoXY(50,21); writeln('|____|__________________|____________|');
   gotoXY(50,23); write  ('Silahkan Masukkan Kode Pesanan Anda : '); readln(pesanan);
   if (pesanan = 1) then
    begin
     gotoXY(50,25); writeln(' Anda memilih menu : Nasi Goreng             ');
     gotoXY(50,26); writeln('             Harga : Rp. 10.000              ');
     gotoXY(50,27); write  ('      Banyak Porsi : ');readln(jumlah); harga:= jumlah*A;
     gotoXY(50,28); writeln('       Total Harga : Rp. ', harga );
     gotoXY(50,30); writeln('             - Terima Kasih -                ');
     gotoXY(50,30); writeln('   Telah Memesan di Restoran Bunda Grande    ');
    end
   else if (pesanan = 2) then
    begin
     gotoXY(50,25); writeln(' Anda memilih menu : Mie Goreng               ');
     gotoXY(50,26); writeln('             Harga : RP. 8.000                ');
     gotoXY(50,27); write  ('     Banyak Porsi  : '); readln(jumlah); harga:= jumlah*B;
     gotoXY(50,28); writeln('       Total Harga : Rp. ', harga);
     gotoXY(50,30); writeln('             - Terima Kasih -                 ');
     gotoXY(50,30); writeln('   Telah Memesan di Restoran Bunda Grande     ');
    end
   else if (pesanan = 3) then
    begin
     gotoXY(50,25); writeln(' Anda memilih menu : Bihun Goreng             ');
     gotoXY(50,26); writeln('             Harga : Rp.8.000                 ');
     gotoXY(50,27); write  ('      Banyak Porsi : '); readln(jumlah); harga:= jumlah*C;
     gotoXY(50,28); writeln('       Total Harga : Rp. ', harga);
     gotoXY(50,30); writeln('             - Terima Kasih -                 ');
     gotoXY(50,30); writeln('   Telah Memesan Di Restoran Bunda Grande     ');
    end
   else if (pesanan = 4) then
    begin
     gotoXY(50,25); writeln(' Anda memilih menu : Soto Daging              ');
     gotoXY(50,26); writeln('             Harga : Rp. 15.000               ');
     gotoXY(50,27); write  ('      Banyak Porsi : '); readln(jumlah); harga:= jumlah*D;
     gotoXY(50,28); writeln('       Total Harga : Rp. ', harga);
     gotoXY(50,30); writeln('             - Terima Kasih -                 ');
     gotoXY(50,30); writeln('   Telah Memesan di Restoran Bunda Grande     ');
    end
   else if (pesanan = 5) then
    begin
     gotoXY(50,25); writeln(' Anda memilih menu : Bubur Ayam               ');
     gotoXY(50,26); writeln('             Harga : Rp. 10.000               ');
     gotoXY(50,27); write  ('      Banyak Porsi : '); readln(jumlah); harga:= jumlah*E;
     gotoXY(50,28); writeln('       Total Harga : Rp. ', harga);
     gotoXY(50,30); writeln('             - Terima Kasih -                 ');
     gotoXY(50,30); writeln('   Telah Memesan di Restoran Bunda Grande     ');
    end
   else
    begin
     gotoXY(55,26); writeln('     KODE ANDA TIDAK VALID ');
     gotoXY(55,28); writeln('[ silahkan masukkan kode ulang ]');
     gotoXY(55,29); writeln('        [ tekan enter ]          ');
    end;
  end

else if (nomor = 2) then
  begin
   gotoXY(34,11); writeln('----------------------------------------------------------------------------');
   gotoXY(50,12); writeln('            MENU MINUMAN             ');
   gotoXY(50,13); writeln(' ___________________________________ ');
   gotoXY(50,14); writeln('| NO |      Minuman     |   Harga   |');
   gotoXY(50,15); writeln('|____|__________________|___________|');
   gotoXY(50,16); writeln('| 1. | Es Teh           | Rp. 5.000 |');
   gotoXY(50,17); writeln('| 2. | Es Jeruk         | Rp. 7.000 |');
   gotoXY(50,18); writeln('| 3. | Jus Alpukat      | Rp. 7.000 |');
   gotoXY(50,19); writeln('| 4. | Jus Mangga       | Rp. 7.000 |');
   gotoXY(50,20); writeln('| 5. | Air Mineral      | Rp. 4.000 |');
   gotoXY(50,21); writeln('|____|__________________|___________|');
   gotoXY(50,23); write  (' Silahkan Masukkan Kode Pesanan Anda : '); readln(pesanan);
   if (pesanan = 1) then
    begin
     gotoXY(50,25); writeln(' Anda memilih menu : Es Teh                ');
     gotoXY(50,26); writeln('             Harga : Rp. 5.000             ');
     gotoXY(50,27); write  ('      Banyak Porsi : '); readln(jumlah); harga := jumlah * F;
     gotoXY(50,28); writeln('       Total Harga : Rp. ', harga);
     gotoXY(50,30); writeln('             - Terima Kasih -              ');
     gotoXY(50,30); writeln('   Telah Memesan di Restoran Bunda Grande  ');
    end
   else if (pesanan = 2) then
    begin
     gotoXY(50,25); writeln(' Anda memilih menu : Es Jeruk              ');
     gotoXY(50,26); writeln('             Harga : Rp. 7.000             ');
     gotoXY(50,27); write  ('      Banyak Porsi : '); readln(jumlah); harga:= jumlah * G;
     gotoXY(50,28); writeln('       Total Harga : Rp. ', harga);
     gotoXY(50,30); writeln('             - Terima Kasih -              ');
     gotoXY(50,30); writeln('   Telah Memesan di Restoran Bunda Grande  ');
    end
   else if (pesanan = 3) then
    begin
     gotoXY(50,25); writeln(' Anda memilih menu : Jus Alpukat           ');
     gotoXY(50,26); writeln('             Harga : Rp. 7.000             ');
     gotoXY(50,27); write  ('      Banyak Porsi : '); readln(jumlah); harga := jumlah * H;
     gotoXY(50,28); writeln('       Total Harga : Rp. ', harga );
     gotoXY(50,30); writeln('             - Terima Kasih -              ');
     gotoXY(50,30); writeln('   Telah Memesan di Restoran Bunda Grande  ');
    end
   else if (pesanan = 4) then
    begin
     gotoXY(50,25); writeln(' Anda memilih menu : Jus Mangga            ');
     gotoXY(50,26); writeln('             Harga : Rp. 7.000             ');
     gotoXY(50,27); write  ('      Banyak Porsi : '); readln(jumlah); harga:= jumlah * I;
     gotoXY(50,28); writeln('       Total Harga : Rp. ', harga );
     gotoXY(50,30); writeln('             - Terima Kasih -              ');
     gotoXY(50,30); writeln('   Telah Memesan di Restoran Bunda Grande  ');
    end
   else if (pesanan = 5) then
    begin
     gotoXY(50,25); writeln(' Anda memilih menu : Air Mineral           ');
     gotoXY(50,26); writeln('             Harga : Rp. 4.000             ');
     gotoXY(50,27); write  ('      Banyak Porsi : '); readln(jumlah); harga:= jumlah * J;
     gotoXY(50,28); writeln('       Total Harga : Rp ', harga );
     gotoXY(50,30); writeln('             - Terima Kasih -              ');
     gotoXY(50,30); writeln('   Telah Memesan di Restoran Bunda Grande  ');
    end
   else
    begin
     gotoXY(55,26); writeln('     KODE ANDA TIDAK VALID      ');
     gotoXY(55,28); writeln('[ silahkan masukkan kode ulang ]');
     gotoXY(55,29); writeln('        [ tekan enter ]         ');
    end;
 end

else if (nomor = 3) then
  begin
   gotoxy(34,11); writeln('-----------------------------------------------------------------------------');
   gotoxy(50,12); writeln('          MENU MAKANAN DAN MINUMAN         ');
   gotoxy(50,13); writeln(' _________________________________________ ');
   gotoXY(50,14); writeln('| NO | Makanan dan Minuman    |   Harga   |');
   gotoXY(50,15); writeln('|____|________________________|___________|');
   gotoXY(50,16); writeln('| 1. | Nasi Goreng dan Es Teh | Rp. 13.000|');
   gotoXY(50,17); writeln('| 2. | Mie Goreng  dan Es Teh | Rp. 12.000|');
   gotoXY(50,18); writeln('| 3. | Soto Daging dan Es Teh | Rp. 18.000|');
   gotoXY(50,19); writeln('|____|________________________|___________|');
   gotoXY(50,21); write  (' Silahkan Masukkan Kode Pesanan Anda : '); readln(pesanan);
   if (pesanan = 1) then
    begin
     gotoXY(50,23); writeln(' Anda memilih menu : Nasi Goreng dan Es Teh ');
     gotoXY(50,24); writeln('             Harga : Rp 13.000              ');
     gotoXY(50,25); write  ('      Banyak Porsi : '); readln(jumlah); harga := jumlah * K;
     gotoXY(50,26); writeln('       Total Harga : Rp. ', harga);
     gotoXY(50,28); writeln('             - Terima Kasih -               ');
     gotoXY(50,29); writeln('   Telah Memesan di Restoran Bunda Grande   ');
     end
   else if (pesanan = 2) then
    begin
     gotoXY(50,23); writeln(' Anda memilih menu : Mie goreng dan Es Teh ');
     gotoXY(50,24); writeln('             Harga : Rp. 12.000            ');
     gotoXY(50,25); write  ('      Banyak Porsi : '); readln(jumlah); harga:= jumlah * L;
     gotoXY(50,26); writeln('       Total Harga : Rp. ', harga);
     gotoXY(50,28); writeln('             - Terima Kasih -              ');
     gotoXY(50,29); writeln('   Telah Memesan di Restoran Bunda Grande  ');
    end
   else if (pesanan = 3) then
    begin
     gotoXY(50,23); writeln(' Anda memilih menu : Soto Daging dan Es Teh ');
     gotoXY(50,24); writeln('             Harga : Rp. 18.000             ');
     gotoXY(50,25); write  ('      Banyak Porsi : '); readln(jumlah); harga:= jumlah * M;
     gotoXY(50,26); writeln('             Harga : Rp. ', harga );
     gotoXY(50,28); writeln('             - Terima Kasih -               ');
     gotoXY(50,29); writeln('   Telah Memesan di Restoran Bunda Grande   ');
    end
   else
    begin
     gotoXY(55,24); writeln('     KODE ANDA TIDAK VALID      ');
     gotoXY(55,26); writeln('[ silakan masukan kode ulang ]  ');
     gotoXY(55,27); writeln('        [ tekan enter ]         ');
    end

  end

  else
  begin
   gotoXY(34,11); writeln('------------------------------------------------------------------------------');
   gotoXY(57,12); writeln(' __________________________');
   gotoXY(57,13); writeln('| Kode Pesanan Tidak Valid |');
   gotoXY(57,14); writeln('|__________________________|');
   gotoXY(55,16); writeln('[ silahkan masukkan kode ulang ]');
   gotoXY(55,17); writeln('         [ tekan enter ]        ');
  end;
  readln;
end.
