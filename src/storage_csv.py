from pathlib import Path
from typing import Protocol
from models import Munkalap
import csv



class Tarolo(Protocol):
    def betolt(self) -> list[Munkalap]:
        ...
    def ment(self, munkalapok: list[Munkalap])-> None:
        ...


class CSVTarolo:
    def __init__(self, fajl: Path):
        self.fajl = fajl


    def betolt(self) -> list[Munkalap]:
        if not self.fajl.exists():
            return []
        with open(self.fajl, "r", encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            return [Munkalap.from_dict(sor) for sor in csv_reader]

    def ment(self, munkalapok: list[Munkalap]):
        fieldnames = [
            "rendszam",
            "tulaj_nev",
            "munka_leiras",
            "ora_dij",
            "ledolgozott_orak",
            "alkatresz_koltseg",
        ]
        self.fajl.parent.mkdir(parents=True, exist_ok=True)
        with open(self.fajl, "w", newline="", encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(m.to_dict() for m in munkalapok)