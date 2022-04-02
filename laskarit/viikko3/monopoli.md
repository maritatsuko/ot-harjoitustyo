```mermaid
    classDiagram
        class Pelaaja
        Pelaaja : nappula
        Pelaaja : sijainti

        class Pelilauta
        Pelilauta : List~int~ ruudut

        class Peli
        Peli : int noppa1
        Peli : int noppa2
        Peli : List pelaajat
        Peli : pelilauta

        Pelaaja --> Pelilauta
        Peli --> Pelaaja
        Peli --> Pelilauta
