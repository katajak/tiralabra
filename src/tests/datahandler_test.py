import os
import unittest
from tempfile import gettempdir
from repositories.datahandler import TiedostonKasittelija
from entities.keychain import Avaimenpera
from entities.inbox import Postilaatikko


class TestKeychain(unittest.TestCase):
    def setUp(self):
        self.tiedostonkasittelija = TiedostonKasittelija()
        self.avaimenpera = Avaimenpera(self.tiedostonkasittelija)
        self.postilaatikko = Postilaatikko(self.tiedostonkasittelija)
        os.chdir(gettempdir())
        with open(f"{gettempdir()+os.sep}asd.priv", "w", encoding="utf-8") as tiedosto:
            tiedosto.write("155302824069287835931228452073974485274966447295390557256488137232285617269050285885610079748411717581562732293757457276021553657214123164594044513833084318571728455601434384083861334019411739007725382157635130316416501591271150733579182063093725285749384453642851848969468073580700567053997744125787772352521;2351265898887889241303674221382310168311115814726944196578419765398529011114364664165107771442622976339667667599564781005593912444576888474915471851404453026705713804856629760272371457146481585724301337795985015427573069674487371274009423441696908683687264583642681811014059452125190720985543948125133740393")
        with open(f"{gettempdir()+os.sep}asd.pub", "w", encoding="utf-8") as tiedosto:
            tiedosto.write("155302824069287835931228452073974485274966447295390557256488137232285617269050285885610079748411717581562732293757457276021553657214123164594044513833084318571728455601434384083861334019411739007725382157635130316416501591271150733579182063093725285749384453642851848969468073580700567053997744125787772352521;65537")
        with open(f"{gettempdir()+os.sep}viesti.msg", "w", encoding="utf-8") as tiedosto:
            tiedosto.write("30901294193478390965942019302439504295738741955007988096976277805663569563654734156403803464660827644648252276157087580725987822700785678480718407796412041073669744549414585656328187610637893144703808444447192412874957139239952803092196823544625268431971183231715912221098375804365514187641828765056789709760")

    def tearDown(self):
        os.remove(f"{gettempdir()+os.sep}asd.priv")
        os.remove(f"{gettempdir()+os.sep}asd.pub")
        os.remove(f"{gettempdir()+os.sep}viesti.msg")

    def test_avaimet_tiedostoista(self):
        self.avaimenpera.lisaa_avaimet_tiedostoista()
        self.assertEqual(self.avaimenpera.avainten_maara(), 2)
        avaimet = []
        for avain in self.avaimenpera.avaimet():
            avaimet.append(avain)
        self.assertEqual(str(avaimet[0]), "asd, yksityinen, 1024 bittiä")
        self.assertEqual(str(avaimet[1]), "asd, julkinen, 1024 bittiä")

    def test_viestit_tiedostoista(self):
        self.postilaatikko.lisaa_viestit_tiedostoista()
        self.assertEqual(self.postilaatikko.viestien_maara(), 1)
        viestit = []
        for viesti in self.postilaatikko.viestit():
            viestit.append(viesti)
        self.assertEqual(viestit[0].viesti, 30901294193478390965942019302439504295738741955007988096976277805663569563654734156403803464660827644648252276157087580725987822700785678480718407796412041073669744549414585656328187610637893144703808444447192412874957139239952803092196823544625268431971183231715912221098375804365514187641828765056789709760)
        self.assertEqual(viestit[0].tiedoston_nimi, "viesti.msg")
