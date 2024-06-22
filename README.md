## Felhasznált technológiák
- Python 3.8
- Flask
- Flask-WTF
- Flask-Login
- Flask-SQLAlchemy
- SQLite
- Pytest
- Charts.js
- Bootstrap
- HTML
- CSS
- JavaScript
- Jinja2
- SQLAlchemy
- Werkzeug

## Funkciók
- Regisztráció
- Bejelentkezés
- Kijelentkezés
- Profil szerkesztése
- Kiadás/Bevétel hozzáadása
- Kiadás/Bevétel szerkesztése
- Kiadás/Bevétel törlése
- Statisztikák megjelenítése

## Szerkezet
- main.py: Az alkalmazás belépési pontja
- models.py: Az adatbázis sémája
- forms.py: Az űrlapok
- routes.py: Az útvonalak
- templates: Az oldalak: 
  - base.html: Az oldal alapja
  - home.html: A főoldal
  - login.html: A bejelentkező oldal
  - sign_up.html: A regisztrációs oldal
  - profile.html: A profil oldal
  - add.html: Az új kiadás/bevétel hozzáadása 
- auth.py: A felhasználókezelés
- views.py: A nézetek, ahol a statisztikák készülnek
- __init__.py: Az alkalmazás inicializálása
- static: A statikus fájlok

## Adatbázis
Az adatbázisban két tábla található:
- User: Az alkalmazás felhasználói
- Expenses: Kiadások és bevételek

