program Luas_Permukaan_Balok;
uses crt;

var
     p,l,t,luas:real;
begin
clrscr;
        writeln('  PROGRAM MENGHITUNG LUAS PERMUKAAN BALOK ');
        writeln('NAMA  : Chindy Aulia Rahmi');
        writeln('NIM   : 2310431012');
        writeln('Shift : 1');
        writeln('==============================================');
        write('Panjang Balok = ');
        readln(p);
        write('Lebar Balok   = ');
        readln(l);
        write('Tinggi Balok  = ');
        readln(t);
        luas:= 2*(p*l+p*t+l*t);
        writeln('Luas Permukaan Balok = ',luas:0:2);
        readln;
end.
