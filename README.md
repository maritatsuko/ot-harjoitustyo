# Ohjelmistotekniikka, harjoitustyö
I am making a **closet application** where the user can *upload pictures* of their clothes and *sort* them.

## Documentation
[Vaatimusmäärittely](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/maritatsuko/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

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
poetry run invoke coverage-test
```
