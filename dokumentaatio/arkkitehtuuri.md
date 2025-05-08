# Arkkitehtuurikuvaus
## Ohjelman rakenne
Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, joka näkyy seuraavasta pakkauskaaviosta:

![Pakkausrakenne ja luokat](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/pakkauskaavio.jpg)

Pakkaus ui vastaa käyttöliittymästä, services sovelluslogiikasta ja repositories tietojen tallenuksesta. Entities vastaa sovelluksen käyttämistä tietokohteista.

## Käyttöliittymä
Käyttöliittymä koostuu näkymistä:
- kirjautuminen
- uuden käyttäjän luominen
- pääkymä
- uuden vaatekappaleen lisääminen

Jokainen näkymä on toteutettu omana luokkanaan ja näkymistä vain yksi kerrallaan on näkyvänä. Näkymien näyttämisestä vasta UI-luokka. Käyttöliittymä on pääosin eristetty sovelluslogiikasta ja se kutsuu ClosetService-luokan metodeja. 

Kun vaatekappaleita lisätään tai kun niiden järjestystä lajitellaan, sovelluksen _show_uploaded_pieces metodi päivittää päänäkymän. 

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat User ja Piece, jotka kuvaavat käyttäjiä ja käyttäjien vaatekappaleita:

```mermaid
 classDiagram
      Piece "*" --> "1" User
      class User{
          id
          username
          password
      }
      class Piece{
          id
          title
          image_path
      }
```

Toiminnallisista kokonaisuuksista vastaa ClosetService. Luokassa on käyttäliittymän toiminnoille omat metodit, esimerkiksi:

- `login(username, password)`
- `upload_piece(title, image_path)`
- `show_image()`

_ClosetService_ pääsee käsiksi käyttäjiin ja kappaleisiin(pieces) tietojen tallennuksesta vastaavan pakkauksessa _repositories_ sijaitsevien luokkien ClosetRepository ja UserRepository kautta.

ClosetService-luokan ja ohjelman muiden osien suhdetta kuvaava luokka/pakkauskaavio:

![Pakkausrakenne ja luokat](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/pakkauskaavio.jpg)

## Tietojen tallennus

Pakkauksen repositories luokat ClosetRepository ja UserRepository vastaavat tietojen tallentamisesta. Molemmat luokat tallentavat tietoa SQlite-tietokantaan. Käyttäjät tallennetaan SQlite-tietokannan tauluun users ja vaatekappaleet tallennetaan SQlite-tietokannan tauluun pieces. Molemmat taulut alustetaan initialize_database.py-tiedostossa. 

## Päätoiminnallisuudet

- Käyttäjän kirjautuminen
- Käyttäjän rekisteröityminen
- Uuden vaatekappaleen lisääminen
- Vaatekappaleen muokkaaminen

## Sekvenssikaavio uuden vaatekappaleen (Piece) lisäämisestä

Uuden Piecen lisäävän upload_view:n "Upload piece"-painikkeen klikkaamisen jälkeen sovelluksen kontrolli etenee seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant ClosetService
  participant ClosetRepository
  participant Piece
  User->>UI: click "Upload piece"
  UI->>ClosetService: upload_piece("my jacket", "src/data/test_data/jacket.png", "pink", "jacket")
  ClosetService->>Piece: Piece("my jacket", "src/data/test_data/jacket.png", "pink", "jacket", "mari")
  ClosetService->>ClosetRepository: upload_piece(Piece("my jacket", "src/data/test_data/jacket.png", "pink", "jacket", "mari"))
  ClosetRepository-->>ClosetService: Piece
  ClosetService-->>UI: Piece
  UI->>UI: initialize()
```
Tapahtumakäsittelijä kutsuu sovellusluokan metodia upload_piece antaen parametriksi vaatteen nimen, kuvan polun, vaatteen värin, vaatteen kategorian ja käyttäjänimen. Sovelluslogiikka luo uuden Piece-olion ja tallettaa sen kutsumalla ClosetRepository:n metodia upload_piece. Tästä seurauksena käyttöliittymä main_view päivittää näytettävät tiedot.

## Sekvenssikaavio vaatekappaleen (Piece) muokkaamisesta

Jo ladatun Piecen muokkaamista käsittelevän edit_view:n "Save edits"-painikkeen klikkaamisen jälkeen sovelluksen kontrolli etenee seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant ClosetService
  participant ClosetRepository
  participant Piece
  User->>UI: click "Save edits"
  UI->>ClosetService: edit_piece("my new jacket", "my jacket", "src/data/test_data/jacket.png", "pink", "jacket")
  ClosetService->>Piece: Piece("my new jacket", "src/data/test_data/jacket.png", "pink", "jacket", "mari")
  ClosetService->>ClosetRepository: edit_piece(Piece("my new jacket", "src/data/test_data/jacket.png", "pink", "jacket", "mari"), "my jacket")
  ClosetRepository-->>ClosetService: Piece
  ClosetService-->>UI: Piece
  UI->>UI: initialize()
```
Tapahtumakäsittelijä kutsuu sovellusluokan metodia edit_piece antaen parametriksi vaatteen nimen, vanhan nimen, kuvan polun, vaatteen värin, vaatteen kategorian ja käyttäjänimen. Sovelluslogiikka luo uuden Piece-olion ja tallettaa sen kutsumalla ClosetRepository:n metodia edit_piece. Tietokantaan päivittyy aiemmin tallennettuun kappaleeseen uudet tiedot. Tästä seurauksena käyttöliittymä main_view päivittää näytettävät tiedot.

## Muut toiminnallisuudet

Myös käyttäjien kirjautuminen ja rekisteröityminen toimivat samalla kaavalla, jossa käyttöliittymän tapahtumakäsittelijä kutsuu sovellusluokan metodia, ja sovelluslogiikka kutsuu sopivan repositorion metodia. Kun palataan käyttöliittymään, aktiivinen näkymä ja ladatut vaattekappaleet päivitetään.
