class SalausJaPurku:
    def salaa_viesti(self, julkinen_avain, viesti):
        return pow(int.from_bytes(viesti.encode(), "big"),
                   julkinen_avain.eksponentti, julkinen_avain.modulus)

    def pura_salaus(self, yksityinen_avain, viesti, pituus):
        try:
            return pow(viesti, yksityinen_avain.eksponentti,
                    yksityinen_avain.modulus).to_bytes(pituus, "big").decode()
        except OverflowError:
            return "Viestin purkaminen epäonnistui. Käytitkö oikeaa avainta?"
