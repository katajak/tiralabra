# Toteutusdokumentti

## Ohjelman yleisrakenne

Käyttöliittymänä toimii sovellus.py. Index.py tiedostossa määritetään oliot ja niille injektoidaan riippuvuudet. Tiedosto alkulukugen.py on vastuussa alkulukujen generoinnista. Tiedosto avaingen.py generoi tarvittavat avaimet. Avaimet itsessään ovat Avain-luokan olioita (avain.py). Nämä Avain-oliot säilytetään Avaimenperä-luokassa (avaimenpera.py), jossa on hyödyllisiä metodeja mm. avainten määrän laskeminen ja avaimen haku nimellä. Viestit ovat Viesti-olioita (viesti.py) ja Viesti-oliot säilytetään Postilaatikko-oliossa (postilaatikko.py). Postilaatikko-olio on rakenteeltaan aika samanlainen kuin Avaimenperä-olio. Avainten ja viestien lukemisen tiedostoista ja kirjoittamisen tiedostoihin vastaa luokka TiedostonKasittelija (tiedostonkasittelija.py). Viestin salauksesta ja salauksen purkamisesta vastaa salauspurku.py.

## Saavutetut aikavaativuudet

Miller-Rabin: O(k log³ n)

Eratostheneen seula: O(n log log n)

## Työn puutteet ja parannusehdotukset

Ohjelmaa voisi laajentaa lisäämällä toiminnallisuuden viestien allekirjoittamiseen.

## Lähteet

https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Complexity

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithmic_complexity
