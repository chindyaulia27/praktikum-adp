program menghitung_volume_bola;
uses crt;
const
        phi = 3.14;
var
        r, volume:real;
begin
clrscr;
        writeln('  PROGRAM MENGHITUNG VOLUME BOLA');
        writeln('NAMA  : Chindy Aulia Rahmi');
        writeln('NIM   : 2310431012');
        writeln('Shift : 1');
        writeln('====================================');
        write('Masukkan nilai jari-jari bola = ');
        readln(r);
        volume:= (4/3)*phi*r*r*r;
        writeln('Volume Bola = ', volume:0:2);
        readln;
end.
