```mermaid
    classDiagram
        class Pelaaja
        Pelaaja : nappula
        Pelaaja : sijainti
        Pelaaja : List omistukset
        Pelaaja : raha

        class Pelilauta
        Pelilauta : aloitusruutu
        Pelilauta : vankila
        Pelilauta : sattuma tai yhteismaa
        Pelilauta : asemat ja laitokset
        Pelilauta : kadut

        class Toiminnot
        Toiminnot : aloitusruutu
        Toiminnot : vankila
        Toiminnot : List sattuma- ja yhteismaakortit
        Toiminnot : kadut

        class Kadut
        Kadut : nimi
        Kadut : omistaja
        Kadut : int talot
        Kadut : int hotelli

        class Peli
        Peli : int noppa1
        Peli : int noppa2
        Peli : List pelaajat
        Peli : pelilauta
        Peli : toiminnot

        Pelaaja --> Pelilauta
        Peli --> Pelaaja
        Peli --> Pelilauta
        Peli --> Toiminnot
        Pelilauta --> Kadut
        Pelilauta --> Toiminnot
        Kadut --> Pelaaja
