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

## Képernyőképek
![image](https://github.com/rendszerkazda/ExpensesApp/assets/146844112/19d5809c-46a2-4391-ae11-45a5ab6f9d35)
![image](https://github.com/rendszerkazda/ExpensesApp/assets/146844112/5cfb5a19-c48c-482b-bc2a-1c90288e1aab)
![image](https://github.com/rendszerkazda/ExpensesApp/assets/146844112/e1852c4e-9bb6-4d13-979e-d88548c94dd7)
![image](https://github.com/rendszerkazda/ExpensesApp/assets/146844112/1593977e-3b36-4083-9fc1-fa03c09aa5bf)
![image](https://github.com/rendszerkazda/ExpensesApp/assets/146844112/5c134ab5-73e4-46ef-b7bb-f33188ec8bcf)
![image](https://github.com/rendszerkazda/ExpensesApp/assets/146844112/df01524b-d31f-49bd-a516-b99c053af255)





