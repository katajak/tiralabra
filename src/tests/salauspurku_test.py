import math
import os
import random
import string
import unittest
from tempfile import NamedTemporaryFile
from logic.alkulukugen import AlkulukuGeneraattori
from logic.avaingen import AvainGeneraattori
from logic.satunnaisgen import SatunnaislukuGeneraattori
from logic.salauspurku import SalausJaPurku
from entities.avaimenpera import Avaimenpera
from entities.postilaatikko import Postilaatikko
from repositories.tiedostonkasittelija import TiedostonKasittelija


class TestEncryptDecrypt(unittest.TestCase):
    def setUp(self):
        self.tiedostonkasittelija = TiedostonKasittelija()
        self.avaimenpera = Avaimenpera(self.tiedostonkasittelija)
        self.postilaatikko = Postilaatikko(self.tiedostonkasittelija)
        self.avaingeneraattori = AvainGeneraattori(AlkulukuGeneraattori(SatunnaislukuGeneraattori()), self.avaimenpera)
        self.salaus_purku = SalausJaPurku(self.postilaatikko)
        self.testitiedosto_1024_yks = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.testitiedosto_1024_jul = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.testitiedosto_2048_yks = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.testitiedosto_2048_jul = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.testitiedosto_viesti = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.avaingeneraattori.generoi_avaimet(1024, "testi1024", self.testitiedosto_1024_yks.name, self.testitiedosto_1024_jul.name)
        self.avaingeneraattori.generoi_avaimet(2048, "testi2048", self.testitiedosto_2048_yks.name, self.testitiedosto_2048_jul.name)

    def tearDown(self):
        self.testitiedosto_1024_yks.close()
        self.testitiedosto_1024_jul.close()
        self.testitiedosto_2048_yks.close()
        self.testitiedosto_2048_jul.close()
        self.testitiedosto_viesti.close()
        os.unlink(self.testitiedosto_1024_yks.name)
        os.unlink(self.testitiedosto_1024_jul.name)
        os.unlink(self.testitiedosto_2048_yks.name)
        os.unlink(self.testitiedosto_2048_jul.name)
        os.unlink(self.testitiedosto_viesti.name)

    def test_encrypt_decrypt(self):
        viesti = "Moi! Tämä on testi. Hui!"
        yksityinen_avain = self.avaimenpera.avaimet()[0]
        julkinen_avain = self.avaimenpera.avaimet()[1]
        self.salaus_purku.salaa_viesti(julkinen_avain, viesti, self.testitiedosto_viesti.name)
        salattu_viesti = self.postilaatikko.viestit()[0]
        purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti)
        self.assertEqual(viesti, purettu_viesti)

    def test_encrypt_decrypt_random_string(self):
        kirjaimet = string.ascii_letters
        viesti = "".join(random.choice(kirjaimet) for _ in range(250))
        yksityinen_avain = self.avaimenpera.avaimet()[2]
        julkinen_avain = self.avaimenpera.avaimet()[3]
        self.salaus_purku.salaa_viesti(julkinen_avain, viesti, self.testitiedosto_viesti.name)
        salattu_viesti = self.postilaatikko.viestit()[0]
        purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti)
        self.assertEqual(viesti, purettu_viesti)

    def test_encrypt_decrypt_vaara_avain(self):
        kirjaimet = string.ascii_letters
        viesti = "".join(random.choice(kirjaimet) for _ in range(250))
        yksityinen_avain = self.avaimenpera.avaimet()[0]
        julkinen_avain = self.avaimenpera.avaimet()[3]
        self.salaus_purku.salaa_viesti(julkinen_avain, viesti, self.testitiedosto_viesti.name)
        salattu_viesti = self.postilaatikko.viestit()[0]
        purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti)
        self.assertEqual("Viestin purkaminen epäonnistui.", purettu_viesti)

    def test_suurin_yhteinen_tekija(self):
        for _ in range(10):
            p = random.randrange(10**1000)
            q = random.randrange(10**1000)
            self.assertEqual(self.avaingeneraattori.syt(p, q), math.gcd(p, q))
