from storage_csv import Tarolo
from models import Munkalap


class MunkalapKezelo:
    def __init__(self, tarolo: Tarolo):
        self._tarolo = tarolo
        self._munkalapok = tarolo.betolt()


    def listaz(self)->list[Munkalap]:
        return list(self._munkalapok)


    def hozzaad(self, m: Munkalap)->None:
        if m not in self._munkalapok:
             self._munkalapok.append(m)
             self._tarolo.ment(self._munkalapok)
        else:
            raise ValueError("Duplikalt munkalap")


    def osszes_bevetel(self)->float:
        return sum(m.osszeg() for m in self._munkalapok)

    def keres_rendszam(self, rendszam: str) -> list[Munkalap]:
        return [m for m in self._munkalapok if m.rendszam == rendszam]

