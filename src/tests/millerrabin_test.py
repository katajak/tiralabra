import unittest
from logic.prime import MillerRabin


# Testeissä käytetään 40 iteraatiota
# https://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes

class TestMillerRabin(unittest.TestCase):
    def setUp(self):
        self.mr = MillerRabin()

    def test_alkulukuja(self):
        self.assertEqual(self.mr.testaa(5, 40), True)
        self.assertEqual(self.mr.testaa(8, 40), False)
        self.assertEqual(self.mr.testaa(7, 40), True)
        self.assertEqual(self.mr.testaa(14, 40), False)
        self.assertEqual(self.mr.testaa(7919 ,40), True)

    def test_suuri_yhdistetty_luku(self):
        self.assertEqual(self.mr.testaa(674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006, 40), False)

    def test_suuri_alkuluku(self):
        self.assertEqual(self.mr.testaa(658022943938739185871458866307770079897174821494059569390843141003821573902527915325288309969616387359598647884041145828085844935102559751264041474960034891373105411778512053365875908139836021077669943205482706750747047089158140435421164720274122715508250725540470763849114048823299427951761411454403, 40), True)
