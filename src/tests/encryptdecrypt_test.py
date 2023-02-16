import unittest
import string
import random
from tempfile import NamedTemporaryFile
from logic.primegen import AlkulukuGeneraattori
from logic.keygen import AvainGeneraattori
from logic.randomgen import SatunnaislukuGeneraattori
from logic.encryptdecrypt import SalausJaPurku
from entities.keychain import Avaimenpera
from datahandler import TiedostonKasittelija


class TestEncryptDecrypt(unittest.TestCase):
    def setUp(self):
        self.avaimenpera = Avaimenpera(TiedostonKasittelija())
        self.avaingeneraattori = AvainGeneraattori(AlkulukuGeneraattori(SatunnaislukuGeneraattori()), self.avaimenpera)
        self.salaus_purku = SalausJaPurku()
        self.testitiedosto = NamedTemporaryFile(encoding="utf-8", mode="w+")

    def test_encrypt_decrypt(self):
        viesti = "Moi! Tämä on testi. Hui!"
        pituus = len(viesti.encode())
        self.avaingeneraattori.generoi_avaimet(1024, "testi1024", self.testitiedosto.name)
        yksityinen_avain = self.avaimenpera.hae_yksityinen_avain_nimella("testi1024")
        julkinen_avain = self.avaimenpera.hae_julkinen_avain_nimella("testi1024")
        salattu_viesti = self.salaus_purku.salaa_viesti(julkinen_avain, viesti)
        purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti, pituus)
        self.assertEqual(viesti, purettu_viesti)

    def test_encrypt_decrypt_random_string(self):
        kirjaimet = string.ascii_letters
        viesti = "".join(random.choice(kirjaimet) for _ in range(255))
        pituus = len(viesti.encode())
        self.avaingeneraattori.generoi_avaimet(2048, "testi2048", self.testitiedosto.name)
        yksityinen_avain = self.avaimenpera.hae_yksityinen_avain_nimella("testi2048")
        julkinen_avain = self.avaimenpera.hae_julkinen_avain_nimella("testi2048")
        salattu_viesti = self.salaus_purku.salaa_viesti(julkinen_avain, viesti)
        purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti, pituus)
        self.assertEqual(viesti, purettu_viesti)

    def test_syt(self):
        self.assertEqual(self.avaingeneraattori.syt(54, 24), 6)
