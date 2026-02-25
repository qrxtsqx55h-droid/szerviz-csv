class MunkalapHiba(Exception):
    pass


class Munkalap:
    def __init__(self,
                 rendszam: str,
                 tulaj_nev: str,
                 munka_leiras: str,
                 ora_dij: int,
                 ledolgozott_orak: float,
                 alkatresz_koltseg: int
                 ):
        if not rendszam.strip():
            raise MunkalapHiba("A rendszam nem lehet ures!")
        if ora_dij < 0:
            raise MunkalapHiba("Az ora_dij nem kehet negativ!")
        if ledolgozott_orak < 0:
            raise MunkalapHiba("Az ledolgozott orak nem lehet negativ!")
        if alkatresz_koltseg < 0:
            raise MunkalapHiba("Az alkatresz_koltseg nem kehet negativ!")

        self.rendszam = rendszam
        self.tulaj_nev = tulaj_nev
        self.munka_leiras = munka_leiras
        self.ora_dij = ora_dij
        self.ledolgozott_orak = ledolgozott_orak
        self.alkatresz_koltseg = alkatresz_koltseg


    def __str__(self):
        return (f"Munkalap adatok:\n"
                f"rendszam: {self.rendszam}\n"
                f"tulaj_nev: {self.tulaj_nev}\n"
                f"munka_leiras: {self.munka_leiras}\n"
                f"ora_dij: {self.ora_dij}\n"
                f"ledolgozott_orak: {self.ledolgozott_orak}\n"
                f"alkatresz_koltseg: {self.alkatresz_koltseg}")


    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self.rendszam}|{self.tulaj_nev}|"
                f"{self.munka_leiras}"
                f"|{self.ora_dij}|"
                f"{self.ledolgozott_orak}|"
                f"{self.alkatresz_koltseg})")


    def to_dict(self)->dict:
        return {"rendszam": self.rendszam,
                "tulaj_nev": self.tulaj_nev,
                "munka_leiras": self.munka_leiras,
                "ora_dij": self.ora_dij,
                "ledolgozott_orak": self.ledolgozott_orak,
                "alkatresz_koltseg": self.alkatresz_koltseg}


    @classmethod
    def from_dict(cls, dct:dict)->"Munkalap":
        return cls(dct["rendszam"],
                   dct["tulaj_nev"],
                   dct["munka_leiras"],
                   int(dct["ora_dij"]),
                   float(dct["ledolgozott_orak"]),
                   int(dct["alkatresz_koltseg"]))


    def osszeg(self)->float:
        total = (self.ora_dij * self.ledolgozott_orak) + self.alkatresz_koltseg
        return total
