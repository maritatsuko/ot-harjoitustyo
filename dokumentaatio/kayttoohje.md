# Instruction Manual / Käyttöohje
Download the source code from the latest [release](https://github.com/maritatsuko/ot-harjoitustyo/releases).
Lataa projektin viimeisimmän [releasen](https://github.com/maritatsuko/ot-harjoitustyo/releases) lähdekoodi.

## Configuration and Installation / Konfigurointi ja Asennus
1. Install dependencies with / Asenna riippuvuudet komennolla
```
poetry install
```
2. Initialize database with / Alusta tietokanta komennolla
```
poetry run invoke init-db
```
3. Start application with / Sovelluksen käynnistys komennolla
```
poetry run invoke start
```

If you do not want to upload your own pictures, you can use the example images from src/data/test_data.

Jos et halua ladata omia kuvia, voit käyttää esimerkkikuvia kansiosta src/data/test_data.

## Logging in / Kirjautuminen

The application starts with the login view. / Sovellus käynnistyy kirjautumisnäkymään:

![](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/login_view.jpeg)

You can log in by typing an existing username and password into the fields and pressing the "Login" button.

Kirjautua voi kirjoittamalla olemassaolevan käyttäjätunnuksen sekä salasanan syötekenttään ja painamalla "Login"-painiketta.

## Creating a new account / Uuden käyttäjän luominen

You can go from the login view to the create account view by clicking the "Create New Account" button.
A new user is created by filling in the details and clicking "Create Account".

Kirjautumisnäkymästä voi siirtyä uuden käyttäjän luomisnäkymään painikkeella "Create New Account".
Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Create Account"-painiketta:

![](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/create_acc_view.jpeg)

If the account creation is successful, you are redirected to the main view.

Jos käyttäjän luominen onnistuu, siirrytään päänäkymään.

## Uploading New Pieces / Uusien vaatekappaleiden (Piece) lataaminen

After a successful login, you're redirected to the main view.

Onnistuneen kirjautumisen myötä siirrytään päänäkymään:

![](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/main_view_1.jpeg)

To upload a new piece, click the "Upload a new piece" button. It takes you to the uploading form.

Jotta pääset lataamaan uuden vaatekappaleen, klikkaa "Upload a new piece"-painiketta. Siitä siirrytään latauslomakkeeseen.

![](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/upload_view_1.jpeg)

Fill in the name of the piece and choose the color and category from the dropdown menus. 
To upload an image (.png, max 800x800px) click the "Select image" button and navigate to your chosen image.
After you've filled out all the information, click the "Upload piece" button to upload the piece and return to the main view.

Täytä vaatekappaleen nimi ja valitse vaatteen väri sekä kategoria avautuvista vaihtoehdoista.
Kuvan (.png, max 800x800px) lataamiseksi klikkaa "Select image"-painiketta ja navigoi valitsemaasi kuvaan.
Kun olet täyttänyt kaikki tiedot vaatteesta, paina "Upload piece"-painiketta lataakseki vaaatteen ja siirtyäkseksi takaisin päänäkymään.

![](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/upload_view_2.jpeg)

## Sorting Uploaded Pieces / Ladattujen vaatekappaleiden järjestys
You can sort the uploaded pieces by Color, Category, and Title (all alphabetically) by clicking the Sort by: dropdown menu.

Voit vaihtaa ladattujen kappaleiden järjestystä aakkosjärjestyksellisten kategorioiden (Color/Väri, Category/Kategoria, Title/Nimi) mukaan klikkaamalla Sort by:n kohdalla olevaa valikkoa.

![](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/main_view_2.jpeg)

## Logging out / Uloskirjautuminen
You can log out by cliking the "Logout" button in the upper righthand corner of the main view. You are then redirected to the login view.

Klikkaamalla päänäkymän oikean ylänurkan painiketta "Logout" käyttäjä kirjautuu ulos sovelluksesta ja palaa takaisin kirjautumisnäkymään.
