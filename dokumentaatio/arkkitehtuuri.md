Laadi ohjelman alustava rakenne luokka- tai pakkauskaaviona (0.75p):
Kaavioon ei tarvitse merkitä kuin sovelluslogiikan kannalta oleelliset luokat

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
