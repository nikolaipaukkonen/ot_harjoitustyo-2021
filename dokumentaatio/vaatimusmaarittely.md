# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellusta käytetään arkeologisen stratigrafian (eli maakerrosten ja muiden materiaalisten ilmiöiden)  määrämuotoiseen dokumentointiin ja tallentamiseen tietokantaan. Stratigrafisen yksikön tietueeseen kirjataan myös yläpuolisen yksikön id-numero, joten eri yksiköiden väliset suhteet on mahdollista rekonstruoida. Kerrosten lisäksi sovelluksessa on omat taulukkonsa löydöille ja näytteille, jotka suhteutuvat myöskin stratigrafisiin kerroksiin. 

 Sovelluksessa on mahdollista luoda erillisiä projekteja, jotka toimivat käytännössä kuin erilliset käyttäjät ja joissa kussakin on oma stratigrafiansa. 

## Projektit
Lähtökohtaisesti kaikki projektit ovat samanlaisia ja niistä löytyy samat toiminnallisuudet. Projektin ollessa auki myös aiemmin merkittyjen yksiköiden poistaminen on mahdollista. 

## Käyttöliittymä
Sovellus koostuu kahdesta näkyämstä
* Luo uusi projekti / Avaa projekti 
* Yksiköiden, löytöjen ja näytteiden luonti ja tarkastelu

## Perusversion tarjoama toiminnallisuus

### Projektin luominen ja muokkaaminen
* Luo uusi projekti, avaa projekti
* Lisää projektiin yksikkö (maa/rakenne/leikkaus, juokseva numero, maaperän kuvaus, minkä päällä jne.)
* Poista yksikkö 
* Lisää löytö
* Lisää näyte

### Projektin vienti ja tarkastelu
* Projektin stratigrafisten yksiköiden tietojen listaaminen
* Vieminen ulos tulosteena (.csv-muodossa)

## Jatkokehitysideoita
Toiminnallisuutta voidaan laajentaa graafisen käyttöliittymän monimutkaistamisella ja erilaisten ulkopuolisten kirjastojen käytöllä. 
* Jo olemassa olevien tietojen muokkaus
* Tietojen visualisointi (verkkona)
* GIS-integraatio (maayksiköiden sitominen kartta-aineistoihin)
* Monimutkaisempi export
* Stratigrafisten ristiriitojen ja mahdottomuuksien huomiointi
* Näyte- ja löytötietokantojen yhteensovittaminen
* Pakolliset ja vapaaehtoiset tietokentät
