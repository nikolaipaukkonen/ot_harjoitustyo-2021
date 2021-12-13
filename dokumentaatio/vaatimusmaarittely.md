# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellusta käytetään arkeologisen stratigrafian (eli maakerrosten ja muiden materiaalisten ilmiöiden)  määrämuotoiseen dokumentointiin ja tallentamiseen tietokantaan. Yksittäisen stratigrafisen yksikön lisäksi sovellukseen toteutetaan mahdollisuus tallentaa stratigrafisia suhteita (vieressä - alla - päällä - leikkaus - jne.) ja luoda jonkinlainen visuaalinen havainnollistus kokonaisuudesta. Kerrosten lisäksi sovelluksessa on omat taulukkonsa löydöille ja näytteille, jotka suhteutuvat myöskin stratigrafisiin kerroksiin.

 Sovelluksessa on mahdollista luoda erillisiä projekteja, jotka toimivat käytännössä kuin erilliset käyttäjät ja joissa kussakin on oma stratigrafiansa.

## Projektit
Lähtökohtaisesti kaikki projektit ovat samanlaisia ja niistä löytyy samat toiminnallisuudet. Projektin ollessa auki myös aiempien merkintöjen muuttamisen tai poistamisen pitää olla mahdollista. 

## Käyttöliittymä
Alkuvaiheessa sovellus koostuu kolmesta näkymästä:
* Luo uusi projekti / Avaa projekti 
* Lisää tai muokkaa stratigrafista yksikköä (alasvetovalikoilla) 
* Lisää löytö (alasvetovalikko) 
* Lisää näyte (alasvetovalikko) 
* Tarkastele projektia (tekstimuotoinen listaus / stratigrafinen piirros tai matriisi)

## Perusversion tarjoama toiminnallisuus

### Projektin luominen ja muokkaaminen
* Luo uusi projekti, avaa projekti, poista projekti *luo / avaa toteutettu*
* Lisää projektiin yksikkö (maa/rakenne/leikkaus, juokseva numero, maaperän kuvaus, väri, minkä alla, minkä päällä jne.) *lisäys toteutettu*
* Muokkaa yksikköä
* Poista yksikkö *toteutettu*
* Lisää löytö *toteutettu*
* Lisää näyte *toteutettu*

### Projektin vienti ja tarkastelu
* Projektin stratigrafisten yksiköiden tietojen listaaminen *toteutettu*
* Visualisointi
* Vieminen ulos tulosteena (txt, xls tai vastaava) *toteutettu .csv*

## Jatkokehitysideoita
Toiminnallisuutta voidaan laajentaa graafisen käyttöliittymän monimutkaistamisella ja erilaisten ulkopuolisten kirjastojen käytöllä. 
* GIS-integraatio (maayksiköiden sitominen kartta-aineistoihin)
* Monimutkaisempi export
* Stratigrafisten ristiriitojen ja mahdottomuuksien huomiointi
* Näyte- ja löytötietokantojen yhteensovittaminen
* Pakolliset ja vapaaehtoiset tietokentät
