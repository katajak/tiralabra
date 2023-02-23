import glob
import operator
from entities.key import Avain
from entities.message import Viesti


class TiedostonKasittelija:
    """Luokka, joka vastaa tiedostojen kirjoituksesta ja lukemisesta.
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
        data = f"{viesti.viesti};{viesti.pituus}"
        with open(tiedoston_nimi, "w", encoding="utf-8") as tiedosto:
            tiedosto.write(data)

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
                    for rivi in file:
                        rivi = rivi.replace("\n", "")
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
                    for rivi in file:
                        rivi = rivi.replace("\n", "")
                        osat = rivi.split(";")
                        viesti = Viesti(int(osat[0]), int(osat[1]), str(tiedosto))
                        viestit.append(viesti)
        return sorted(viestit, key=operator.attrgetter("tiedoston_nimi"))
