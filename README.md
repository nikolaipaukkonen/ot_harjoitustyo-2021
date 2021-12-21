# Stratigraphy Database Manager
### Ohjelmistotekniikka 2021

Tämä sovellus on tarkoitettu arkeologisen stratigrafisen aineiston hallinnointiin sekä sen yhdistämiseen mm. löytö- ja näytetietoihin. Sovelluksella voidaan luoda useita erillisiä projekteja, jotka ovat itsenäisiä suhteessa toisiinsa.

Kurssin laskuharjoitukset ovat [erillisessä kansiossa](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/blob/main/laskarit/laskarit_readme.md).

Toinen release: [Viikko 6 deadline](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/releases/tag/viikko6)

Ensimmäinen release: [Viikko 5 deadline](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/releases).

## Python-versio
Ohjelma on kehitetty Pythonin versiolla 3.8.10.

## Dokumentaatio
* [Käyttöohje](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/blob/main/dokumentaatio/kayttoohje.md#k%C3%A4ytt%C3%B6ohje)
* [Vaatimusmäärittely](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/blob/main/dokumentaatio/vaatimusmaarittely.md)
* [Arkkitehtuurikuvaus](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/blob/main/dokumentaatio/arkkitehtuurikuvaus.md)
* Testausdokumentti
* [Työaikakirjanpito](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/blob/main/dokumentaatio/tuntikirjanpito.md)

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

Pylint-tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
``` 


