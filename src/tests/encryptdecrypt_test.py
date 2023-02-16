import unittest
import string
import random
from tempfile import NamedTemporaryFile
from logic.primegen import AlkulukuGeneraattori
from logic.keygen import AvainGeneraattori
from logic.randomgen import SatunnaislukuGeneraattori
from logic.encryptdecrypt import SalausJaPurku
from entities.keychain import Avaimenpera
from entities.inbox import Postilaatikko
from repositories.datahandler import TiedostonKasittelija


class TestEncryptDecrypt(unittest.TestCase):
    def setUp(self):
        self.tiedostonkasittelija = TiedostonKasittelija()
        self.avaimenpera = Avaimenpera(self.tiedostonkasittelija)
        self.postilaatikko = Postilaatikko(self.tiedostonkasittelija)
        self.avaingeneraattori = AvainGeneraattori(AlkulukuGeneraattori(SatunnaislukuGeneraattori()), self.avaimenpera)
        self.salaus_purku = SalausJaPurku(self.postilaatikko)
        self.testitiedosto = NamedTemporaryFile(encoding="utf-8", mode="w+")

    def test_encrypt_decrypt(self):
        viesti = "Moi! Tämä on testi. Hui!"
        self.avaingeneraattori.generoi_avaimet(1024, "testi1024", self.testitiedosto.name)
        yksityinen_avain = self.avaimenpera.hae_yksityinen_avain_nimella("testi1024")
        julkinen_avain = self.avaimenpera.hae_julkinen_avain_nimella("testi1024")
        self.salaus_purku.salaa_viesti(julkinen_avain, viesti, self.testitiedosto.name)
        salattu_viesti = self.postilaatikko.hae_viesti_nimella("viesti.msg")
        purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti)
        self.assertEqual(viesti, purettu_viesti)

    def test_encrypt_decrypt_random_string(self):
        kirjaimet = string.ascii_letters
        viesti = "".join(random.choice(kirjaimet) for _ in range(255))
        self.avaingeneraattori.generoi_avaimet(2048, "testi2048", self.testitiedosto.name)
        yksityinen_avain = self.avaimenpera.hae_yksityinen_avain_nimella("testi2048")
        julkinen_avain = self.avaimenpera.hae_julkinen_avain_nimella("testi2048")
        self.salaus_purku.salaa_viesti(julkinen_avain, viesti, self.testitiedosto.name)
        salattu_viesti = self.postilaatikko.hae_viesti_nimella("viesti.msg")
        purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti)
        self.assertEqual(viesti, purettu_viesti)

    def test_syt(self):
        self.assertEqual(self.avaingeneraattori.syt(54, 24), 6)
