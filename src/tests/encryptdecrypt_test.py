import unittest
import string
import random
from logic.primegen import AlkulukuGeneraattori
from logic.keygen import AvainGeneraattori
from logic.randomgen import SatunnaislukuGeneraattori
from logic.encryptdecrypt import SalausJaPurku
from entities.key import Avain


class TestPrimes(unittest.TestCase):
    def setUp(self):
        self.avaingeneraattori = AvainGeneraattori(AlkulukuGeneraattori(SatunnaislukuGeneraattori()))
        self.salaus_purku = SalausJaPurku()

    def test_encrypt_decrypt(self):
        yksityinen_avain = Avain()
        julkinen_avain = Avain()
        viesti = "Moi! Tämä on testi. Hui!"
        pituus = len(viesti.encode())
        self.avaingeneraattori.generoi_avaimet(1024, yksityinen_avain, julkinen_avain)
        salattu_viesti = self.salaus_purku.salaa_viesti(julkinen_avain, viesti)
        purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti, pituus)
        self.assertEqual(viesti, purettu_viesti)

    def test_encrypt_decrypt_random_string(self):
        yksityinen_avain = Avain()
        julkinen_avain = Avain()
        kirjaimet = string.ascii_letters
        viesti = "".join(random.choice(kirjaimet) for _ in range(255))
        pituus = len(viesti.encode())
        self.avaingeneraattori.generoi_avaimet(2048, yksityinen_avain, julkinen_avain)
        salattu_viesti = self.salaus_purku.salaa_viesti(julkinen_avain, viesti)
        purettu_viesti = self.salaus_purku.pura_salaus(yksityinen_avain, salattu_viesti, pituus)
        self.assertEqual(viesti, purettu_viesti)

    def test_syt(self):
        self.assertEqual(self.avaingeneraattori.syt(54, 24), 6)
