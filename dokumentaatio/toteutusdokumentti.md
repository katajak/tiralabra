# Toteutusdokumentti

## Ohjelman yleisrakenne

Käyttöliittymänä toimii app.py. Index.py tiedostossa määritetään oliot ja niille injektoidaan riippuvuudet. Tiedosto primegen.py on vastuussa alkulukujen generoinnista. Tiedosto keygen.py generoi tarvittavat avaimet. Avaimet itsessään ovat Avain-luokan olioita (key.py). Nämä Avain-oliot säilytetään Avaimenperä-luokassa (keychain.py), jossa on hyödyllisiä metodeja mm. avainten määrän laskeminen ja avaimen haku nimellä. Viestin salauksesta ja salauksen purkamisesta vastaa encryptdecrypt.py.

## Työn puutteet ja parannusehdotukset

Toivon että lopullisessa versiossa saan tehtyä avainten ja viestin tallennuksen silleen että voi toisen henkilön julkisen avaimen drag&drop tyylillä pistää johonkin kansioon, ja sitten voisi salata sillä toisen henkilön julkisella avaimella viestin, jonka voi "lähettää" toiselle purettavaksi.
