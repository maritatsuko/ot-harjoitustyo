# Arkkitehtuurikuvaus
## Ohjelman alustava rakenne luokka- ja pakkauskaavioina

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

![Pakkausrakenne ja luokat](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/pakkauskaavio.jpg)

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
  UI->>ClosetService: upload_piece("jacket", "src/data/test_data/jacket.png")
  ClosetService->>Piece: Piece("jacket", "src/data/test_data/jacket.png")
  ClosetService->>ClosetRepository: upload_piece(Piece("jacket", "src/data/test_data/jacket.png"))
  ClosetRepository-->>ClosetService: Piece
  ClosetService-->>UI: Piece
  UI->>UI: initialize()
```
Tapahtumakäsittelijä kutsuu sovellusluokan metodia upload_piece antaen parametriksi vaatteen nimen ja kuvan polun. Sovelluslogiikka luo uuden Piece-olion ja tallettaa sen kutsumalla ClosetRepository:n metodia upload_piece. Tästä seurauksena käyttöliittymä main_view päivittää näytettävät tiedot.
