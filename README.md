# ClosetApp (Ohjelmistotekniikka, harjoitustyö)
ClosetApp is an application for storing and sorting items in your closet.
You can add pictures of your clothes and sort through them alphabetically, by color, and by category.
You can also edit the pieces you have uploaded.

# Releases

[loppupalautus / final](https://github.com/maritatsuko/ot-harjoitustyo/releases/tag/loppupalautus)

[viikko6](https://github.com/maritatsuko/ot-harjoitustyo/releases/tag/viikko6)

[viikko5](https://github.com/maritatsuko/ot-harjoitustyo/releases/tag/viikko5)

## Documentation
[Vaatimusmäärittely](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)

[Käyttöohje / Instruction manual](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

## Installation

1. Install dependencies with
```
poetry install
```
2. Initialize database with
```
poetry run invoke init-db
```
3. Start application with
```
poetry run invoke start
```

## Tests
Tests can be run with
```
poetry run invoke test
```

## Test coverage report can be generated with
```
poetry run invoke coverage-report
```

## Pylint can be run with
```
poetry run invoke lint
```
