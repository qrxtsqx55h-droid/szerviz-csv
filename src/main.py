from pathlib import Path

from storage_csv import CSVTarolo
from service import MunkalapKezelo
from models import Munkalap, MunkalapHiba


tarolo = CSVTarolo(Path('data/munkalapok.csv'))
kezelo = MunkalapKezelo(tarolo)

def szoveg_input(kerdes: str):
    while True:
        adat = input(kerdes)
        if not adat.strip():
            print("Hiba: Ez a mező nem maradhat üres!")
            continue
        return adat

def szam_input(kerdes: str, tipus=float):
    while True:
        try:
            adat = tipus(input(kerdes))
            if adat < 0:
                print('HIBA: Az ertek nem lehet negativ!')
                continue
            return adat
        except ValueError as e:
            print(f"Hiba: Kérlek adj meg egy érvényes számot ({tipus.__name__})!")


print('.' * 50)
print("    Munkalapkezelo software Autoszervizeknek!")
print('.' * 50)

while True:
    try:
        print(f"1. Uj munkalap\n"
              f"2. Listazas\n"
              f"3. Osszes bevetel\n"
              f"4. Keres rendszamra\n"
              f"0. Kilepes")
        print('-' * 50)
        valasztas = szam_input('Valassz: ', tipus = int)
        if valasztas == 1:
            rendszam = szoveg_input('Az auto rendszama: ')
            tulaj_nev = szoveg_input('A tulaj neve: ')
            munka_leiras = szoveg_input('A munka leirasa: ')
            ora_dij = szam_input('Az ora dij: ', tipus= int)
            ledolgozott_orak = szam_input('A ledolgozott orak: ')
            alkatresz_koltseg = szam_input('A alkatresz koltseg: ', tipus= int)
            print('-' * 50)

            kezelo.hozzaad(Munkalap(rendszam,
                                    tulaj_nev,
                                    munka_leiras,
                                    ora_dij,
                                    ledolgozott_orak,
                                    alkatresz_koltseg)
                           )
        elif valasztas == 2:
            for k in kezelo.listaz():
                print()
                print('-' * 50)
                print(k)
                print('-' * 50)
                print()
        elif valasztas == 3:
            print()
            print('-' * 50)
            print(f'Osszes bevetel = {kezelo.osszes_bevetel()}')
            print('-' * 50)
            print()
        elif valasztas == 4:
            print()
            print('-' * 50)
            rendszam = szoveg_input('Keres rendszam: ')
            talalat = kezelo.keres_rendszam(rendszam)
            if talalat:
                for t in talalat:
                    print(t)
            else:
                print("Nincs találat.")
            print()
            print('-' * 50)
        elif valasztas == 0:
            break

        else:
            print("Ismeretlen menüpont!")

    except ValueError as e:
        print(f"Duplikacio/rosz szam {e}")
    except MunkalapHiba as e:
        print(f"Validacio hiba {e}")
