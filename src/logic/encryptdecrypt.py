from entities.message import Viesti


class SalausJaPurku:
    """Luokka, joka vastaa viestin salaamisesta ja salauksen purkamisesta.
    """
    def __init__(self, postilaatikko):
        self.postilaatikko = postilaatikko

    def salaa_viesti(self, julkinen_avain, viesti, tiedoston_nimi):
        """Metodi, joka vastaa viestin salaamisesta.
        Viesti muunnetaan kokonaisluvuksi, ennen kuin se voidaan salata.
        Palauttaa kokonaisluvun, joka on salattu viesti.
        """
        viesti_olio = Viesti(pow(int.from_bytes(viesti.encode(), "big"), julkinen_avain.eksponentti,
                                 julkinen_avain.modulus), len(viesti.encode()), tiedoston_nimi)
        self.postilaatikko.lisaa_viesti(viesti_olio, tiedoston_nimi)

    def pura_salaus(self, yksityinen_avain, viesti):
        """Metodi, joka vastaa viestin salauksen purkamisesta.
        Salatulle viestille tehdään tarvittavat laskutoimitukset ja
        lopuksi muunnetaan merkkijonoksi.
        Palauttaa alkuperäisen viestin merkkijonona.
        """
        try:
            return pow(viesti.viesti, yksityinen_avain.eksponentti,
                    yksityinen_avain.modulus).to_bytes(viesti.pituus, "big").decode()
        except Exception:
            return "Viestin purkaminen epäonnistui."
