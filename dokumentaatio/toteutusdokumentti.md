# Toteutusdokumentti

## Ohjelman yleisrakenne

Käyttöliittymänä toimii sovellus.py. Index.py tiedostossa määritetään oliot ja niille injektoidaan riippuvuudet. Tiedosto alkulukugen.py on vastuussa alkulukujen generoinnista. Tiedosto avaingen.py generoi tarvittavat avaimet. Avaimet itsessään ovat Avain-luokan olioita (avain.py). Nämä Avain-oliot säilytetään Avaimenperä-luokassa (avaimenpera.py), jossa on hyödyllisiä metodeja mm. avainten määrän laskeminen ja avaimen haku nimellä. Viestit ovat Viesti-olioita (viesti.py) ja Viesti-oliot säilytetään Postilaatikko-oliossa (postilaatikko.py). Postilaatikko-olio on rakenteeltaan aika samanlainen kuin Avaimenperä-olio. Avainten ja viestien lukemisen tiedostoista ja kirjoittamisen tiedostoihin vastaa luokka TiedostonKasittelija (tiedostonkasittelija.py). Viestin salauksesta ja salauksen purkamisesta vastaa salauspurku.py.

## Työn puutteet ja parannusehdotukset

Sellainen UI jossa voi tehdä valinnan nuolinäppäimillä. Ohjelmistotuotantokurssin miniprojektissa opin tekemään tälläisen pyinquirer moduulilla mutta en ollut täysin tyytyväinen siihen, kun siinä oli bugeja. Vaikka se ei määrittelydokumenttiin kuulunut niin jos jää aikaa, niin teen mahdollisesti myös vertaisarviossa mainitun viestien allekirjoittamisen.
