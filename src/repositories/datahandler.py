import glob
import operator
from entities.key import Avain
from entities.message import Viesti


class TiedostonKasittelija:
    """Luokka, joka vastaa tiedostojen kirjoituksesta ja lukemisesta.
    """
    def __init__(self):
        pass

    def kirjoita_avain_tiedostoon(self, avain, tiedoston_nimi):
        """Metodi kirjoittaa avaimen tiedostoon.
        """
        data = f"{avain.nimi};{avain.tyyppi};{avain.bittimaara};{avain.modulus};{avain.eksponentti}"
        with open(tiedoston_nimi, "w", encoding="utf-8") as tiedosto:
            tiedosto.write(data)

    def kirjoita_viesti_tiedostoon(self, viesti, tiedoston_nimi):
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
                with open(tiedosto, "r", encoding="utf-8") as file:
                    for rivi in file:
                        rivi = rivi.replace("\n", "")
                        osat = rivi.split(";")
                        avain = Avain(str(osat[0]), str(osat[1]),
                                      int(osat[2]), int(osat[3]), int(osat[4]))
                        avaimet.append(avain)
        return sorted(avaimet, key=operator.attrgetter("nimi"))

    def lue_viestit_tiedostoista(self):
        viestit = []
        luettavat = ["*.msg"]
        for tiedostomuoto in luettavat:
            for tiedosto in glob.glob(tiedostomuoto):
                with open(tiedosto, "r", encoding="utf-8") as file:
                    for rivi in file:
                        rivi = rivi.replace("\n", "")
                        osat = rivi.split(";")
                        viesti = Viesti(int(osat[0]), int(osat[1]))
                        viestit.append(viesti)
        return viestit
