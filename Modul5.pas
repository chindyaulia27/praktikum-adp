program Caesar_Chiper;
uses crt;

var
 k,i,caesar,karakter  : integer;
 kata,enkripsi : string;

const
 huruf : array[1..26] of char = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
                                  't','u','v','w','x','y','z');
begin
clrscr;
 writeln('           PROGRAM CAESAR CHIPER');
 writeln('-----------------------------------------------');
 write ('Masukkan nilai penggeseran huruf (k) dari 1-26 : '); readln(k);writeln;

 while ((k < 0) or (k > 26)) do
  begin
  writeln;
  writeln(' ------------------------------- ');
  writeln('| KODE YANG ANDA MASUKKAN SALAH |');
  writeln(' ------------------------------- ');
  writeln;
  write ('Masukkan nilai penggeseran huruf (k) dari 1-26 : '); readln(K);
  writeln;
  end;

 if ((k > 0) and (k < 27)) then
  begin
   write ('Kata / Kalimat yang ingin dienkripsikan : '); readln(kata);
   for i:= 1 to length(kata) do
    begin
    if kata[i] in ['a'..'z','A'..'Z'] then
     begin
      if (kata[i] >= 'A') and (kata[i] <='Z') then
       kata[i] := Chr(Ord(kata[i])+ 32);

      karakter := 0;
      while (karakter < 26) and (huruf[karakter+1] <> kata [i]) do
      karakter := karakter + 1;
      caesar := ( karakter + k ) mod 26;
      enkripsi := enkripsi + huruf [caesar+1];
     end
    else
    enkripsi := enkripsi + kata [i];
    end;
   writeln('teks enkripsi : ', enkripsi);
 end;

readln;
end.
