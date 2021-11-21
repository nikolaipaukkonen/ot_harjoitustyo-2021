# Arkkitehtuurikuvaus

## Käyttöliittymä

Ohjelman käyttöliittymässä on kolme erilaista näkymää. 
- Avaa / luo uusi projekti -näkymä
- Tietojen lisääminen projektiin
- Tietojen tarkastelu 

Nämä on toteutettu tai toteutetaan omina luokkinaan UI-luokan päällä. Projektin avaamisen ja luomisen hoitaa IntroView-luokka ja tietojen lisäämisen MainView. InspectView näyttää tiedot taulukkonäkymänä.

## Sovelluslogiikka

Tällä hetkellä sovelluksen looginen tietomalli perustuu osan locus_database oleville metodeille. Näitä ovat mm. check_db, create_locus ja create_find. Näitä operoidaan Locus, Find ja Sample -olioilla, jotka locus_databasen metodit muuntavat SQLite-käskyiksi. Sovelluslogiikkaa tullaan eriyttämään jatkossa kerroksellisemmaksi erillisten tallentamisesta vastaavien repositioiden avulla.
