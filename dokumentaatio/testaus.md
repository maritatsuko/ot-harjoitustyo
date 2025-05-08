# Testausdokumentti

Ohjelmaa on testattu automatisoiduin yksikkö- ja integraatiotestein unittestillä sekä manuaalisesti järjestelmätasolla.

## Yksikkö- ja integraatiotestaus

Piecen kuvapolkujen testaukseen käytetään kansiota [test_data](https://github.com/maritatsuko/ot-harjoitustyo/tree/main/src/data/test_data)

### Sovelluslogiikka

Sovelluslogiikasta vastaavaa ClosetService -luokkaa testataan [TestClosetService](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/src/tests/service_test.py) testiluokalla.

### Repositorio-luokat

Repositorioluokkia ClosetRepository ja UserRepository testataan luokilla [TestClosetRepository](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/src/tests/closet_repository_test.py)
ja [TestUserRepository](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/src/tests/user_repository_test.py).

### Testauskattavuus

Käyttöliittymää lukuunotta sovelluksen testauksen haaraumakattavuus on 82%.
![](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/coverage_report.jpeg)

Testaamatta jäi index.py -tiedosto, joka käynnistää sovelluksen. Jäi myös testaamatta joitakin tyhjiä/vääriä syötteitä eri kenttiin.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja testattu [käyttöohjeen](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md) kuvaamalla tavalla Linux-ympäristössä.
Sovellusta on testattu luomalla useampi käyttäjä ja lataamalla käyttäjille samoja sekä erilaisia vaatteita.

### Toiminallisuudet

Kaikki [määrittelydokumentin](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md) ja käyttöohjeen toiminnallisuudet on käyty läpi.
Kaikkien toiminnallisuuksien yhteydessä syötekenttiä on yritetty täyttää myös virheellisillä ja tyhjillä arvoilla.

## Sovellukseen jääneet laatuongelmat

Sovellus ei anna järkevää ilmoitusta jos SQLite tietokantaa ei ole alustettu.
