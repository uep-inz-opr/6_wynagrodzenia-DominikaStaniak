import random
import math

class Pracownik:
  def __init__(self, imie, brutto):
    self.imie=imie
    self.brutto=float(brutto)

il_pracownikow=int(input())
pracownicy = []
for linia in range(il_pracownikow):
  imie = input()
  brutto = input()
  pracownik = Pracownik(imie, float(brutto))
  pracownicy.append(pracownik)

def skladki(pracownicy):
  suma_kosztow_pracodawcy = 0
  for Pracownik in pracownicy:
      skladki = round((Pracownik.brutto * 0.0976) + (Pracownik.brutto * 0.015) + (Pracownik.brutto * 0.0245) + (Pracownik.brutto * 0.0976) + (Pracownik.brutto * 0.065) + (Pracownik.brutto * 0.0196) + (Pracownik.brutto * 0.0245) + (Pracownik.brutto * 0.01),2)
      netto = round(Pracownik.brutto - (skladki + ((Pracownik.brutto - skladki)*0.09)  + (((Pracownik.brutto - 111.25 - skladki)*0.18) - ((Pracownik.brutto - skladki)*0.0775))),2)
      koszt = round(Pracownik.brutto + ((Pracownik.brutto * 0.0976) + (Pracownik.brutto * 0.065) + (Pracownik.brutto * 0.0196) + (Pracownik.brutto * 0.0245) + (Pracownik.brutto * 0.01)),2)
      print (Pracownik.imie + " " + "{:.2f}".format(netto) + " " +"{:.2f}".format(skladki) + " " + "{:.2f}".format(koszt))
      suma_kosztow_pracodawcy += koszt
  print("{:.2f}".format(suma_kosztow_pracodawcy))
  
skladki(pracownicy)
