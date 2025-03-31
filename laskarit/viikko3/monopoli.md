```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula

    Aloitusruutu "1" -- Ruutu : Tyyppi
    Monopolipeli -- Aloitusruutu : Sijainti
    Monopolipeli -- Vankila : Sijainti
    Vankila "1" -- Ruutu : Tyyppi
    Sattuma Ja Yhteismaa -- Ruutu : Tyyppi
    Sattuma Ja Yhteismaa -- Toiminnot : Sattuma ja yhteismaa kortit
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Toiminnot -- Ruutu : Toiminto
    Asemat Ja Laitokset -- Pelaaja
    Asemat Ja Laitokset -- Ruutu : Tyyppi
    Normaalit Kadut -- Ruutu : Tyyppi
    Normaalit Kadut -- Pelaaja
    Normaalit Kadut "1" -- "0..4" Talo
    Normaalit Kadut "1" -- "0..1" Hotelli

    class Asemat Ja Laitokset{
        pelaaja
    }
    class Normaalit Kadut{
        talot
        hotelli
        pelaaja
    }
    class Pelaaja{
        raha
        omistukset
    }
    class Toiminnot{
        aloitusruutu
        vankila
        sattuma- ja yhteismaakortit
        kadut
    }
```
