import random
import math

class Pracownik:
  def __init__(self, imie, brutto):
    self.imie=imie
    self.brutto=float(brutto)

il_pracownikow=int(input())
pracownicy = []
for linia in range(il_pracownikow):
  imie, brutto = input().split()
  pracownik = Pracownik(imie, brutto)
  pracownicy.append(pracownik)

def skladki(pracownicy):
  suma_kosztow_pracodawcy = 0
  for Pracownik in pracownicy:
      skladki_1 = round((Pracownik.brutto * 0.0976) + (Pracownik.brutto * 0.015) + (Pracownik.brutto * 0.0245),2)
      skladki_2= round((Pracownik.brutto * 0.0976) + (Pracownik.brutto * 0.065) + (Pracownik.brutto * 0.0193) + (Pracownik.brutto * 0.0245) + (Pracownik.brutto * 0.001),2)
      podst_skladki_zdro = round((pracownik.brutto - skladki_1),2)
      skladka_zdro_pob= round((podst_skladki_zdro * 0.09),2)
      skladka_zdro_odl=round((podst_skladki_zdro*0.0775),2)
      kup = 111.25
      zal_pod_doch_odl = round((round(((round(Pracownik.brutto - kup - skladki_1))* 0.18),2)-46.33),2)
      zal_pod_doch_pob = round((zal_pod_doch_odl - skladka_zdro_odl))
      netto = round((Pracownik.brutto - skladki_1 - skladka_zdro_pob - zal_pod_doch_pob),2)
      koszt = round((Pracownik.brutto + skladki_2),2)
      suma_skladki = skladki_1 + skladki_2
      print (Pracownik.imie + " " + "{:.2f}".format(netto) + " " +"{:.2f}".format(skladki_2) + " " + "{:.2f}".format(koszt))
      suma_kosztow_pracodawcy += koszt
  print("{:.2f}".format(suma_kosztow_pracodawcy))
  
skladki(pracownicy)
