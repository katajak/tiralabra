class TiedostonKasittelija:
    def __init__(self):
        pass

    def kirjoita_tiedostoon(self, avain, tiedoston_nimi):
        data = f"{avain.nimi};{avain.tyyppi};{avain.bittimaara};{avain.modulus};{avain.eksponentti}"
        with open(tiedoston_nimi, "w", encoding="utf-8") as tiedosto:
            tiedosto.write(data)
