from math import pi
class fizyka:

 def silaciezkosci():
    m = float(input("masa ="))
    print("Fg =", {m*10})

 def silawypadkowa():
    m = float(input("masa = "))
    a = float(input("przyspieszenie = "))
    print(f"Fw =", {m*a})

 def silawyporu():
    d = float(input("gestosc ="))
    V = float(input("objetosc ="))
    print("Fwyporu = ",{d*V*10} )

 def predkosc():
    s = float(input("droga ="))
    t = float(input("czas ="))
    print("v =" ,{s/t})

 def silanacisku():
    d = float(input("gestosc ="))
    h = float(input("wysokosc ="))
    print("FN =" ,{d*h*10})

 def silatarcia():
    Fn = float(input("sila sprezystosci ="))
    f = float(input("opor powietrza ="))
    print("Ft =", {Fn*f})

 def przyspieszenie():
    v = float(input("predkosc ="))
    t = float(input("czas ="))
    print(f"Wynik to {v/t}")

 def oporelektryczny():
    U = float(input("natezenie elektryczne = "))
    I = float(input("natezenie pradu = "))
    print(f"Wynik to {U/I}")

 def mocmechaniczna():
    t = float(input("czas ="))
    W = float(input("praca ="))
    print(f"Wynik to {W/t}")

 def pracamechaniczna():
    F = float(input("sila ="))
    s = float(input("droga ="))
    print(f"Wynik to {F*s}")
 
 def pedciala():
    m = float(input("masa = "))
    v = float(input("predkosc ="))
    print(f"Wynik to {m*v}")