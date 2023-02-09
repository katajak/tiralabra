class SalausJaPurku:
    """Luokka, joka vastaa viestin salaamisesta ja salauksen purkamisesta.
    """
    def salaa_viesti(self, julkinen_avain, viesti):
        """Metodi, joka vastaa viestin salaamisesta.
        Viesti muunnetaan kokonaisluvuksi, ennen kuin se voidaan salata.
        Palauttaa kokonaisluvun, joka on salattu viesti.
        """
        return pow(int.from_bytes(viesti.encode(), "big"),
                   julkinen_avain.eksponentti, julkinen_avain.modulus)

    def pura_salaus(self, yksityinen_avain, viesti, pituus):
        """Metodi, joka vastaa viestin salauksen purkamisesta.
        Salatulle viestille tehdään tarvittavat laskutoimitukset ja
        lopuksi muunnetaan merkkijonoksi.
        Palauttaa alkuperäisen viestin merkkijonona.
        """
        try:
            return pow(viesti, yksityinen_avain.eksponentti,
                    yksityinen_avain.modulus).to_bytes(pituus, "big").decode()
        except Exception:
            return "Viestin purkaminen epäonnistui. Käytitkö oikeaa avainta?"
