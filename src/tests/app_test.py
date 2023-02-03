import unittest
from unittest.mock import Mock
from ui.app import UI
from logic.primegen import AlkulukuGeneraattori
from logic.keygen import AvainGeneraattori

class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, syote):
        return self.inputs.pop(0)

    def kirjoita(self, syote):
        self.outputs.append(syote)

class TestUI(unittest.TestCase):
    def setUp(self):
        self.alkulukugeneraattori_mock = Mock(wraps=AlkulukuGeneraattori())
        self.avaingeneraattori_mock = Mock(wraps=AvainGeneraattori(self.alkulukugeneraattori_mock))

    def test_voi_poistua_ohjelmasta(self):
        io = StubIO(["q"])
        sovellus = UI(io, None)
        sovellus.suorita()
        self.assertEqual(sovellus.run, False)

    def test_vaara_syote(self):
        io = StubIO(["asd", "q"])
        sovellus = UI(io, self.avaingeneraattori_mock)
        sovellus.suorita()
        self.assertEqual(sovellus.run, False)
        self.avaingeneraattori_mock.generoi_avaimet.assert_not_called()

    def test_avainten_generointi_kutsuu_oikeaa_funktiota_oikealla_arvolla_1024(self):
        io = StubIO(["1", "1", "q"])
        sovellus = UI(io, self.avaingeneraattori_mock)
        sovellus.suorita()
        self.avaingeneraattori_mock.generoi_avaimet.assert_called_with(1024)

    def test_avainten_generointi_kutsuu_oikeaa_funktiota_oikealla_arvolla_2048(self):
        io = StubIO(["1", "2", "q"])
        sovellus = UI(io, self.avaingeneraattori_mock)
        sovellus.suorita()
        self.avaingeneraattori_mock.generoi_avaimet.assert_called_with(2048)

    def test_avainten_generointi_vaara_valinta(self):
        io = StubIO(["1", "r", "q"])
        sovellus = UI(io, self.avaingeneraattori_mock)
        sovellus.suorita()
        self.avaingeneraattori_mock.generoi_avaimet.assert_not_called()
