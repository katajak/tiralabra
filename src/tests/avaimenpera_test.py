import os
import unittest
from tempfile import NamedTemporaryFile
from entities.avaimenpera import Avaimenpera
from entities.avain import Avain
from repositories.tiedostonkasittelija import TiedostonKasittelija


class TestKeychain(unittest.TestCase):
    def setUp(self):
        self.avaimenpera = Avaimenpera(TiedostonKasittelija())
        self.testitiedosto = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.julkinen_avain = Avain("hyvä avain", "julkinen", 1024, 2116953895613963430716550748887608776530532428256447102580544051743259563453612543294580643603640768916502311227622591711503177812166740110551776204418975773335531960692700102394377893090969103864502984858772442396601688293681490067675268111658307084803156802676067493785943284641865490566684167021453073627, 65537)
        self.yksityinen_avain = Avain("toinen avain", "yksityinen", 1024, 2116953895613963430716550748887608776530532428256447102580544051743259563453612543294580643603640768916502311227622591711503177812166740110551776204418975773335531960692700102394377893090969103864502984858772442396601688293681490067675268111658307084803156802676067493785943284641865490566684167021453073627, 768618001222733110058445230477144984322505136493311546239590547495778893028040808515717021141471719736456848736763653657860721669293797105918481388897100439594437873278665058401690652845386824319532083259469497857528266755565333558396626216557333754894754853895450021786975583440002174633008035752348580633)

    def tearDown(self):
        self.testitiedosto.close()
        os.unlink(self.testitiedosto.name)

    def test_avainten_listaus(self):
        kaikki_avaimet = self.avaimenpera.avaimet()
        self.assertEqual(len(kaikki_avaimet), 0)
        self.avaimenpera.lisaa_avain(self.yksityinen_avain, self.testitiedosto.name)
        self.avaimenpera.lisaa_avain(self.julkinen_avain, self.testitiedosto.name)
        kaikki_avaimet = self.avaimenpera.avaimet()
        self.assertEqual(len(kaikki_avaimet), 2)
        self.assertEqual(kaikki_avaimet[0], self.yksityinen_avain)
        self.assertEqual(kaikki_avaimet[1], self.julkinen_avain)
        self.assertEqual("toinen avain, yksityinen, 1024 bittiä", str(self.yksityinen_avain))
        self.assertEqual("hyvä avain, julkinen, 1024 bittiä", str(self.julkinen_avain))

        yksityiset_avaimet = self.avaimenpera.yksityiset_avaimet()
        self.assertEqual(len(yksityiset_avaimet), 1)
        self.assertEqual(yksityiset_avaimet[0], self.yksityinen_avain)

        julkiset_avaimet = self.avaimenpera.julkiset_avaimet()
        self.assertEqual(len(julkiset_avaimet), 1)
        self.assertEqual(julkiset_avaimet[0], self.julkinen_avain)

    def test_avainten_maara(self):
        self.assertEqual(self.avaimenpera.avainten_maara(), 0)
        self.avaimenpera.lisaa_avain(self.yksityinen_avain, self.testitiedosto.name)
        self.assertEqual(self.avaimenpera.avainten_maara(), 1)
        self.avaimenpera.lisaa_avain(self.julkinen_avain, self.testitiedosto.name)
        self.assertEqual(self.avaimenpera.avainten_maara(), 2)
