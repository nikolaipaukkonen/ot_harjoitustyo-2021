# Testausdokumentti

Ohjelmaa on testattu automaattisilla yksikkötesteillä. Lisäksi on tehty manuaalisia testejä.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Keskeisintä `locus_database` -luokkaa testataan `locus_database_test`-testiluokalla. Testiluokka luo testitietokannan ja siihen erilaisia testitietueita. 

### Testauskattavuus

Testauskattavuus on 95%.

![](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/blob/main/dokumentaatio/testikattavuus.png?raw=true)

Graafisen käyttöliittymän osat jäivät testaamisen ulkopuolelle. Myös joitakin poikkeuksia yms. on testaamatta. 

## Järjestelmätestaus

Manuaalista testausta on suoritettu ohjelmalle eri kehitysvaiheissa.

### Asennus

Sovellus on haettu ja sitä on testattu erilaisissa Linux-ympäristöissä, mm. Cubblilla ja Manjarolla. 

### Toiminnallisuudet

Kaikki listatut toiminnallisuudet on testattu. Myös joitakin virheellisiä syötteitä on testattu, mutta ei kovinkaan kattavasti.

### Sovellukseen jääneet laatunogelmat

Virheilmoitukset eivät ole kattavia ja ne tulevat ainoastaan terminaaliin, eli graafinen käyttöliittymä ei anna palautetta esimerkiksi virheellisistä syötteistä. Lisäksi SQL-komentoihin meneviä syötteitä ei ole sanitisoitu mitenkään, joten halutessaan käyttäjä voi injektoida komentoja ja saada aikaan ei-toivottuja toimintoja. 
