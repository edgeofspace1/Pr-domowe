from cz1 import fizyka

print("""
Co obliczyc?
1. sila ciezkosci
2. sila wypadkowa
3. sila wyporu
4. predkosc 
5. sila nacisku
6. sila tarcia
7. przyspieszenie
8. opor elektryczny
9. moc mechaniczna
10. praca mechaniczna
11. ped ciala
""")
ktorewybrac = int(input(""))

if ktorewybrac == 1:
 fizyka.silaciezkosci()
elif ktorewybrac ==2 :
 fizyka.silawypadkowa()
elif ktorewybrac == 3:
 fizyka.siawyporu()
elif ktorewybrac == 4:
 fizyka.predkosc()
elif ktorewybrac == 5:
 fizyka.silanacisku()
elif ktorewybrac == 6:
 fizyka.silatarcia()
elif ktorewybrac == 7:
 fizyka.przyspieszenie()
elif ktorewybrac == 8:
 fizyka.oporelektryczny()
elif ktorewybrac == 9:
 fizyka.mocmechaniczna()
elif ktorewybrac == 10:
 fizyka.pracamechaniczna()
elif ktorewybrac == 11:
 fizyka.pedciala()
else:
    print("blad")




