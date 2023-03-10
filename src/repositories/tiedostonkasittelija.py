import operator
import os
import glob
from datetime import datetime
from entities.avain import Avain
from entities.viesti import Viesti


class TiedostonKasittelija:
    """Luokka, joka on vastuussa tiedostojen kirjoituksesta ja lukemisesta.
    """
    def kirjoita_avain_tiedostoon(self, avain, tiedoston_nimi):
        """Metodi kirjoittaa avaimen tiedostoon.
        """
        data = f"{avain.modulus};{avain.eksponentti}"
        with open(tiedoston_nimi, "w", encoding="utf-8") as tiedosto:
            tiedosto.write(data)

    def kirjoita_viesti_tiedostoon(self, viesti, tiedoston_nimi):
        """Metodi kirjoittaa viestin tiedostoon.
        """
        with open(tiedoston_nimi, "w", encoding="utf-8") as tiedosto:
            tiedosto.write(str(viesti.viesti))

    def lue_avaimet_tiedostoista(self):
        """Metodi lukee avaimet tiedostoista ja tekee niistä avain-olioita.
        Palauttaa listan avain-olioista.
        """
        avaimet = []
        luettavat = ["*.priv", "*.pub"]
        for tiedostomuoto in luettavat:
            for tiedosto in glob.glob(tiedostomuoto):
                if tiedostomuoto == "*.priv":
                    nimi = tiedosto[:-5]
                    tyyppi = "yksityinen"
                else:
                    nimi = tiedosto[:-4]
                    tyyppi = "julkinen"

                with open(tiedosto, "r", encoding="utf-8") as file:
                    rivi = file.readline()
                    osat = rivi.split(";")
                    if len(bin(int(osat[0]))[2:]) > 4000:
                        bittimaara = 4096
                    elif len(bin(int(osat[0]))[2:]) > 2000:
                        bittimaara = 2048
                    else:
                        bittimaara = 1024

                    avain = Avain(nimi, tyyppi, bittimaara, int(osat[0]), int(osat[1]))
                    avaimet.append(avain)
        return sorted(avaimet, key=operator.attrgetter("nimi"))

    def lue_viestit_tiedostoista(self):
        """Metodi lukee viestit tiedostoista ja tekee niistä viesti-olioita.
        Palauttaa listan viesti-olioista.
        """
        viestit = []
        luettavat = ["*.msg"]
        for tiedostomuoto in luettavat:
            for tiedosto in glob.glob(tiedostomuoto):
                with open(tiedosto, "r", encoding="utf-8") as file:
                    rivi = file.readline()
                    muokkausaika = (datetime.fromtimestamp(os.path.getmtime(tiedosto))
                                    .isoformat(sep=" ", timespec="seconds"))
                    viesti = Viesti(int(rivi), tiedosto, muokkausaika)
                    viestit.append(viesti)
        return sorted(viestit, key=operator.attrgetter("muokkausaika"))
