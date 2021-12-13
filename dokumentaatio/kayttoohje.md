# Käyttöohje

Lataa projektin viimeisin [release](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/releases/tag/viikko6)

## Ohjelman käynnistäminen

Ennen käyttöä on asennettava riippuvuudet komennolla

```bash
poetry install
```

Minkä jälkeen voit suorittaa alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Käynnistä ohjelma komennolla:

```
poetry run invoke start
```

## Projektin valitseminen

Sovellus avautuu näkymään, jossa voi joko luoda uuden projektin tai jatkaa vanhan täydentämistä. Vanhan ohjelman voi avata yksinkertaisesti kirjoittamalla sen nimen nimikenttään. Kenttää ei voi jättää tyhjäksi.

## Tietokannan täydentäminen ja tarkastelu

Kun tietokanta on luotu tai valittu, voidaan sitä alkaa täyttää. 

Ensimmäisellä rivillä on valikko, jolla luodaan uusi stratigrafinen yksikkö (locus). Yksikölle syötetään tyyppi, nimi (jonka on oltava uniikki), kuvaus, paksuus senteissä sekä mahdollinen yläpuolella olevan toisen yksikön id. 

Toisella rivillä voidaan syöttää eri yksiköissä tehtyjä löytöjä tietokantaan. Löytöön syötetään tyyppi, löydön ajoitus, paino sekä yksikkö, jossa löytö oli.

Kolmantena voidaan syöttää näyte. Näytteelle valitaan sen tyyppi (hiili- tai maanäyte, tai muu näyte) sekä yksikkö, josta näyte otettiin. 

Tiedot voidaan viedä ulos helpommin luettavaan csv-muotoon. Expot locus data -nappula luo erilliset csv-tiedostot yksiköille, löydöille ja näytteille.

Lisäksi yksiköitä voidaan poistaa id-numeron perusteella.

Alimpana ovat nappulat yksikkö- ja löytötaulukoiden näkymän päivittämistä varten. Switch project -nappulasta ohjelma palaa alkunäkymään, jossa voi vaihtaa projektia.

![Käyttöliittymä](https://github.com/nikolaipaukkonen/ot_harjoitustyo-2021/blob/main/dokumentaatio/ui_example.png?raw=true)
