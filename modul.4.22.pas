program segitiga_angka;
uses crt;

var
  i, j, t:Longint;

begin
clrscr;
  writeln('  MENCETAK POLA SEGITIGA ANGKA ');
  writeln('--------------------------------');writeln;
  write  ('Masukkan tinggi segitiga : '); readln(t); writeln;
  writeln('Berikut tampilan pola segitiga dengan tinggi ',t,' >>>>');

  if (t>=0) then
  begin
   for i:=1 to t do
   begin
    for j:=1 to i do
     begin
     write (j,' ');
     end;
    writeln('');
   end;
  end

  else if (t<0) then
  begin
   writeln(' _____________________________');
   writeln('|    KODE ANDA TIDAK VALID    |');
   writeln(' ----------------------------- ');
  end;
readln;
end.
