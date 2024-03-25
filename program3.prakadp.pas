Program tabel_perkalian_dan_penjumlahan;
uses crt;

var
 n,pilih, i, j,k: integer;

label
 ulang_1,ulang_2;

begin
clrscr;
 ulang_1:
 writeln('  TABEL PENJUMLAHAN DAN PERKALIAN NXN');
 writeln('---------------------------------------');
 write  ('Silahkan masukkan nilai n (1-10): ');readln(n);
 writeln('Anda memilih tabel berukuran : ', n ,' x ', n);

 ulang_2:
  if ((n>=1) and (n<=10)) then
   begin
    writeln('');
    writeln('Berikut beberapa tampilan menu yang dapat ditampilkan : ');
    writeln('              1. tabel perkalian n x n ');
    writeln('              2. tabel penjumlahan n x n ');
    writeln('              3. keluar  ');
    writeln('');
    write  (' Silahkan masukkan nomor kode menu yang ingin ditampilkan : '); readln(pilih);
    writeln('-------------------------------------------------------------');
     if (pilih=1) then
      begin
       writeln('');
       writeln(' Berikut adalah tampilan tabel perkalian ',n,' x ',n);
       writeln('');
       write('|  x |');
        for i:=1 to n do
         write( i:4,' |' );writeln;
        for i:=1 to n do
         begin
          write('|', i:3,' |');
          for j:=1 to n do
           begin
            write(i*j:4,' |');
           end;
          writeln;
         end;
       writeln;
       writeln('[silahkan tekan enter untuk kembali ke opsi menu]');
       readln;
       goto ulang_2;
      end

     else if (pilih=2) then
      begin
       writeln('');
       writeln(' Berikut adalah tampilan tabel perkalian ',n,' x ',n);
       writeln('');
       write('|  + |');
        for i:=1 to n do
         write(i:4,' |'); writeln;
        for i:=1 to n do
        begin
         write('|', i:3,' |');
         for j:=1 to n do
          begin
           write(i+j:4,' |');
          end;
         writeln;
        end;
       writeln;
       writeln('[silahkan tekan enter untuk kembali ke opsi menu]');
       readln;
       goto ulang_2;
      end

     else if (pilih=3) then
      begin
       writeln('       Anda memilih opsi 3 : keluar ');
       writeln('  [tekan enter untuk keluar dari program] ');
      end
    end

  else if n>10 then
   begin
      writeln('');
      writeln(' _____________________________________ ');
      writeln('|Kode Yang Anda masukkan tidak sesuai |');
      writeln('|       silahkan tekan enter          |');
      writeln(' ------------------------------------- ');
      readln;
      goto ulang_1;
   end

  else if n > 10 then
   begin
    readln;
    goto ulang_1;
   end;

readln;
end.
