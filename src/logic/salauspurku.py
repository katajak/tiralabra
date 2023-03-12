from datetime import datetime
from entities.viesti import Viesti


class SalausJaPurku:
    """Luokka, joka on vastuussa viestin salaamisesta ja salauksen purkamisesta.
    """
    def __init__(self, postilaatikko):
        self.postilaatikko = postilaatikko

    def salaa_viesti(self, julkinen_avain, viesti, tiedoston_nimi):
        """Metodi, joka on vastuussa viestin salaamisesta.
        Argumentit:
        julkinen avain = avain-olio
        viesti = salaamaton viesti str-muodossa
        tiedoston_nimi = haluttu tiedoston nimi

        Viesti muunnetaan kokonaisluvuksi, ennen kuin se voidaan salata.
        Lisää postilaatikko-olioon viesti-olion ja kirjoittaa viesin tiedostoon.
        """
        viesti_olio = Viesti(pow(int.from_bytes(viesti.encode(), "big"), julkinen_avain.eksponentti,
                                 julkinen_avain.modulus), tiedoston_nimi,
                                 datetime.now().isoformat(sep=" ", timespec="seconds"))
        self.postilaatikko.lisaa_viesti(viesti_olio, tiedoston_nimi)

    def pura_salaus(self, yksityinen_avain, viesti):
        """Metodi, joka on vastuussa viestin salauksen purkamisesta.
        Salatulle viestille tehdään tarvittavat laskutoimitukset ja
        lopuksi muunnetaan merkkijonoksi.
        Palauttaa alkuperäisen viestin merkkijonona.
        """
        purettu_viesti_int = pow(viesti.viesti, yksityinen_avain.eksponentti,
                                 yksityinen_avain.modulus)
        pituus = purettu_viesti_int.bit_length()//8+1
        return pow(viesti.viesti, yksityinen_avain.eksponentti,
                   yksityinen_avain.modulus).to_bytes(pituus, "big").decode()
