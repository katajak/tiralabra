import glob
import operator
from entities.key import Avain


class TiedostonKasittelija:
    """Luokka, joka vastaa tiedostojen kirjoituksesta ja lukemisesta.
    """
    def __init__(self):
        pass

    def kirjoita_tiedostoon(self, avain, tiedoston_nimi):
        """Metodi kirjoittaa avaimen tiedostoon.
        """
        data = f"{avain.nimi};{avain.tyyppi};{avain.bittimaara};{avain.modulus};{avain.eksponentti}"
        with open(tiedoston_nimi, "w", encoding="utf-8") as tiedosto:
            tiedosto.write(data)

    def lue_tiedostot(self):
        """Metodi lukee avaimet tiedostoista ja tekee niistä avain-olioita.
        Palauttaa listan avain-olioista.
        """
        avaimet = []
        luettavat = ["*.priv", "*.pub"]
        for tiedostomuoto in luettavat:
            for tiedosto in glob.glob(tiedostomuoto):
                with open(tiedosto, "r", encoding="utf-8") as file:
                    for rivi in file:
                        rivi = rivi.replace("\n", "")
                        osat = rivi.split(";")
                        avain = Avain(str(osat[0]), str(osat[1]),
                                      int(osat[2]), int(osat[3]), int(osat[4]))
                        avaimet.append(avain)
        return sorted(avaimet, key=operator.attrgetter("nimi"))
