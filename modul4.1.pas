program bilangan_sempurna;
uses crt;

var
   i, sum, a :longint;

begin
clrscr;
 writeln('      BILANGAN SEMPURNA [ PERFECT NUMBER ]  ');
 writeln('------------------------------------------------');
 writeln;
 write('Silahkan masukkan angka yang ingin anda periksa : '); readln(a); writeln;

 sum:=0;

 for i:=1 to a div 2 do
  begin
   if a mod i = 0 then
   begin
     sum:= sum + i;
   end
  end;

 if (sum = a) then
  begin
  writeln(a, ' adalah bilangan sempurna/perfect number'); writeln;
  end
 else
  begin
  writeln(a,' "bukan" bilangan sempurna/perfect number'); writeln;
  end;

 if a mod 2 = 0 then
  begin
  writeln(a, ' adalah bilangan "genap"');
  end
 else
 begin
 writeln(a, ' adalah bilangan "ganjil"');
 end;

readln;
end.
