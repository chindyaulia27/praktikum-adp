program perkalian_sederhana;
uses crt;

var
   a,b,perkalian:real;
begin
clrscr;
        writeln(' PROGRAM PERKALIAN SEDERHANA ');
        writeln('NAMA  : Chindy Aulia Rahmi' );
        writeln('NIM   : 2310431012' );
        writeln('Shift : 1');
        writeln('===============================');
        write('Nilai 1 : ');
        readln(a);
        write('Nilai 2 : ');
        readln(b);
        perkalian:= a*b;
        writeln('Hasil Perkalian nilai 1 dan nilai 2 = ',perkalian :0:2);
        readln;
end.
