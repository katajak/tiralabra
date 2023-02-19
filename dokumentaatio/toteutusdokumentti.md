# Toteutusdokumentti

## Ohjelman yleisrakenne

Käyttöliittymänä toimii app.py. Index.py tiedostossa määritetään oliot ja niille injektoidaan riippuvuudet. Tiedosto primegen.py on vastuussa alkulukujen generoinnista. Tiedosto keygen.py generoi tarvittavat avaimet. Avaimet itsessään ovat Avain-luokan olioita (key.py). Nämä Avain-oliot säilytetään Avaimenperä-luokassa (keychain.py), jossa on hyödyllisiä metodeja mm. avainten määrän laskeminen ja avaimen haku nimellä. Viestit ovat Viesti-olioita (message.py) ja Viesti-oliot säilytetään Postilaatikko-oliossa (inbox.py). Postilaatikko-olio on rakenteeltaan aika samanlainen kuin Avaimenperä-olio. Avainten ja viestien lukemisen tiedostoista ja kirjoittamisen tiedostoihin vastaa luokka TiedostonKasittelija (datahandler.py). Viestin salauksesta ja salauksen purkamisesta vastaa encryptdecrypt.py.

## Työn puutteet ja parannusehdotukset

En ole täysin tyytyväinen siihen että avaimiin ja viestitiedostoihin tallennetaan "turhaa" tietoa (esim. nimi, bittimäärä, viestin pituus). Yritän tätä parantaa tulevilla viikoilla. Myös sellainen UI jossa voi tehdä valinnan nuolinäppäimillä. Ohjelmistotuotantokurssin miniprojektissa opin tekemään tälläisen pyinquirer moduulilla mutta en ollut täysin tyytyväinen siihen, kun siinä oli bugeja. Vaikka se ei määrittelydokumenttiin kuulunut niin jos jää aikaa, niin teen mahdollisesti myös vertaisarviossa mainitun viestien allekirjoittamisen.
