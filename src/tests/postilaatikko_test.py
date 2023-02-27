import os
import unittest
from datetime import datetime
from tempfile import NamedTemporaryFile
from entities.postilaatikko import Postilaatikko
from entities.viesti import Viesti
from repositories.tiedostonkasittelija import TiedostonKasittelija


class TestKeychain(unittest.TestCase):
    def setUp(self):
        self.postilaatikko = Postilaatikko(TiedostonKasittelija())
        self.testitiedosto1 = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.testitiedosto2 = NamedTemporaryFile(encoding="utf-8", mode="w+", delete=False)
        self.viesti1 = Viesti(14563222416692617621639651159849580600294441838424712128985821341884853680095131712046345756882783088318076349709887379463883842398986861115303631904044570680571161508826859668931872959587447500190734600160152946759836997694639866111460145812442077287961603781563626106631332898616109905391351264128515623451, "testiviesti.msg", datetime.now().isoformat(sep=" ", timespec="seconds"))
        self.viesti2 = Viesti(9094938843149366171466902020006300145290327274789419483038627060565636763756316674057873053352664541540378346713888724990810729287414915817222159113376039357645738586181792302637632548017904049687704882957381598595238834452096769011216042546486038318635665989327370313535860605311556451157638575577449594173, "toinen.msg", datetime.now().isoformat(sep=" ", timespec="seconds"))

    def tearDown(self):
        self.testitiedosto1.close()
        self.testitiedosto2.close()
        os.unlink(self.testitiedosto1.name)
        os.unlink(self.testitiedosto2.name)

    def test_viestin_listaus(self):
        viestit = self.postilaatikko.viestit()
        self.assertEqual(len(viestit), 0)
        self.postilaatikko.lisaa_viesti(self.viesti1, self.testitiedosto1.name)
        self.postilaatikko.lisaa_viesti(self.viesti2, self.testitiedosto2.name)
        viestit = self.postilaatikko.viestit()
        self.assertEqual(len(viestit), 2)
        self.assertEqual(viestit[0], self.viesti1)
        self.assertEqual(viestit[1], self.viesti2)
        aika1 = datetime.fromtimestamp(os.path.getmtime(self.testitiedosto1.name)).isoformat(sep=" ", timespec="seconds")
        aika2 = datetime.fromtimestamp(os.path.getmtime(self.testitiedosto2.name)).isoformat(sep=" ", timespec="seconds")
        self.assertEqual(f"testiviesti.msg, kirjoitettu {aika1}", str(self.viesti1))
        self.assertEqual(f"toinen.msg, kirjoitettu {aika2}", str(self.viesti2))

    def test_viestien_nimet(self):
        self.postilaatikko.lisaa_viesti(self.viesti1, self.testitiedosto1.name)
        self.postilaatikko.lisaa_viesti(self.viesti2, self.testitiedosto2.name)
        nimet = self.postilaatikko.viestien_nimet()
        self.assertEqual(len(nimet), 2)
        self.assertEqual(nimet[0], self.viesti1.tiedoston_nimi)
        self.assertEqual(nimet[1], self.viesti2.tiedoston_nimi)
