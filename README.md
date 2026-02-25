# 🚗 Szerviz CSV – Munkalapkezelő CLI

Egyszerű, CSV-alapú munkalapkezelő alkalmazás autószervizek számára.

## 📌 Funkciók

- ✅ Új munkalap rögzítése
- 📋 Munkalapok listázása
- 💰 Összes bevétel számítása
- 🔍 Keresés rendszám alapján
- 💾 CSV-alapú perzisztencia
- 🌿 Git branch workflow

---

## 🏗 Projekt struktúra

    ```szerviz_csv/
    │
    ├── src/
    │   ├── models.py
    │   ├── storage_csv.py
    │   ├── service.py
    │   └── main.py
    │
    ├── data/
    │   └── munkalapok.csv
    │
    ├── .gitignore
    └── README.md```

---

## ▶️ Futtatás

Virtuális környezet aktiválása után:

```bash
python src/main.py