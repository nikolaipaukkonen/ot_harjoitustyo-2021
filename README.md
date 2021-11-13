# Stratigraphy Database Manager
### Ohjelmistotekniikka 2021

Tämä sovellus on tarkoitettu arkeologisen stratigrafisen aineiston hallinnointiin sekä sen yhdistämiseen mm. löytö- ja näytetietoihin. Sovelluksella voidaan luoda useita erillisiä projekteja, jotka ovat itsenäisiä suhteessa toisiinsa.

## Python-versio


## Dokumentaatio
* Käyttöohje
* [Vaatimusmäärittely](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/blob/main/harjoitustyo/dokumentaatio/vaatimusmaarittely.md)
* Arkkitehtuurikuvaus
* Testausdokumentti
* [Työaikakirjanpito](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/blob/main/harjoitustyo/dokumentaatio/tuntikirjanpito.md)

## Asennus
1. Asenna ensin riippuvuudet:
```bash
ṕoetry install
```

2. Käynnistä sovelluksen graafinen käyttöliittymä:
```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
