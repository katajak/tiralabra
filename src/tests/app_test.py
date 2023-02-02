import unittest
from ui.app import UI

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
        pass

    def test_voi_poistua_ohjelmasta(self):
        io = StubIO(["q"])

        sovellus = UI(io, None, None)
        sovellus.suorita()

        self.assertEqual(sovellus.run, False)
