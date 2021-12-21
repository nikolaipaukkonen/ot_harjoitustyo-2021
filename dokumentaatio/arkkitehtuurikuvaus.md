# Arkkitehtuurikuvaus

## Käyttöliittymä

Ohjelman käyttöliittymässä on kolme erilaista näkymää. 
- Avaa / luo uusi projekti -näkymä
- Tietojen lisääminen projektiin

Nämä on toteutettu tai toteutetaan omina luokkinaan UI-luokan päällä. Projektin avaamisen ja luomisen hoitaa IntroView-luokka ja tietojen lisäämisen MainView. InspectView näyttää tiedot taulukkonäkymänä.

## Sovelluslogiikka

Sovelluksen looginen tietomalli perustuu osan locus_database oleville metodeille. Näitä ovat mm. check_db, create_locus ja create_find. Näitä operoidaan Locus, Find ja Sample -olioilla, jotka locus_databasen metodit muuntavat SQLite-komennoiksi. Sovelluslogiikkaa tullaan eriyttämään jatkossa kerroksellisemmaksi erillisten tallentamisesta vastaavien repositioiden avulla.

![Sovelluslogiikka](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/blob/main/dokumentaatio/P%C3%A4%C3%A4toiminnallisuudet.png?raw=true)

## Tietojen tallennus

Kun projekti luodaan, syntyy .db-muotoinen tietokantatiedosto projektikansioon. Ohjelman ajon aikana ohjelma lukee `read_db_name()` funktiolla avoinna olevan tiedoston nimen väliaikaisesta db_list.txt-tiedostosta. 

Tiedot on mahdollista viedä .csv-muodossa projektikansioon funktiolla `export_data()`, joka kirjoittaa erilliset kolme tiedostoa yksiköille, löydöille ja näytteille. 

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä

Graafisen käyttöliittymän koodi on toisteista ja vaikeasti seurattavaa. Näkymä ja eri tietueiden lisäystoimintojen id-kohdat eivät myöskään päivity reaaliajassa, vaan projekti täytyy sulkea ja avata uudelleen. Lisäksi käyttöliittymä on ruma. 
