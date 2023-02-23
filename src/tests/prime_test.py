import sympy
import unittest
from secrets import randbelow
from logic.primegen import AlkulukuGeneraattori
from logic.randomgen import SatunnaislukuGeneraattori

# Miller-Rabinissa käytetään 40 iteraatiota
# https://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes

class StubRandomBits:
    def __init__(self):
        self.inputs = []

    def satunnainen_int_mr(self, n):
        return 2+randbelow(n-3)

    def satunnainen_int_n_bittia(self, n):
        return self.inputs.pop(0)

    def lisaa_getrandbits(self, l):
        for i in l:
            self.inputs.append(i)


class TestPrimes(unittest.TestCase):
    def setUp(self):
        self.primes = AlkulukuGeneraattori(SatunnaislukuGeneraattori())

    def test_suuri_yhdistetty_luku(self):
        self.assertEqual(self.primes.tarkista_onko_alkuluku(674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006746328388800674632838880067463283888006), False)

    def test_suuri_alkuluku(self):
        self.assertEqual(self.primes.tarkista_onko_alkuluku(658022943938739185871458866307770079897174821494059569390843141003821573902527915325288309969616387359598647884041145828085844935102559751264041474960034891373105411778512053365875908139836021077669943205482706750747047089158140435421164720274122715508250725540470763849114048823299427951761411454403), True)

    def test_generoiduilla_alkuluvuilla(self):
        alkuluvut = self.primes.generoi_alkuluvut(1024)
        self.assertTrue(self.primes.tarkista_onko_alkuluku(alkuluvut[0]))
        self.assertTrue(self.primes.tarkista_onko_alkuluku(alkuluvut[1]))

    def test_generoidut_alkuluvut_oikeasti_alkulukuja_sympy(self):
        for _ in range(100):
            alkuluvut = self.primes.generoi_alkuluvut(1024)
            self.assertTrue(sympy.isprime(alkuluvut[0]))
            self.assertTrue(sympy.isprime(alkuluvut[1]))

    def test_eratostheneen_seula(self):
        sympy_seula = list(sympy.sieve.primerange(0, 1000))
        alkuluvut = self.primes.generoi_pienet_alkuluvut(1000)
        for i in range(len(alkuluvut)):
            self.assertEqual(alkuluvut[i], sympy_seula[i])

    def test_miller_rabin_pienilla_alkuluvuilla(self):
        alkuluvut = self.primes.generoi_pienet_alkuluvut(10**5)
        alkuluvut.pop(0)
        alkuluvut.pop(0)
        for alkuluku in alkuluvut:
            self.assertTrue(self.primes.miller_rabin(alkuluku, 40))

    def test_miller_rabin(self):
        for _ in range(100):
            alkuluku = sympy.randprime(0, 10**100)
            self.assertTrue(self.primes.miller_rabin(alkuluku, 40))

    def test_koko_tarkistus(self):
        for _ in range(100):
            alkuluku = sympy.randprime(0, 10**100)
            self.assertTrue(self.primes.tarkista_onko_alkuluku(alkuluku))

    def test_esitarkistus_pienilla_alkuluvuilla(self):
        alkuluvut = self.primes.generoi_pienet_alkuluvut(10**5)
        for alkuluku in alkuluvut:
            self.assertTrue(self.primes.esitarkistus(alkuluku))

    def test_esitarkistus_ja_miller_rabin_pienilla_alkuluvuilla(self):
        alkuluvut = self.primes.generoi_pienet_alkuluvut(10**5)
        for alkuluku in alkuluvut:
            self.assertTrue(self.primes.tarkista_onko_alkuluku(alkuluku))

    def test_kaksi_samaa_alkulukua(self):
        fake_random = StubRandomBits()
        primes = AlkulukuGeneraattori(fake_random)
        fake_random.lisaa_getrandbits([170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 162259276829213363391578010288127])
        alkuluvut = primes.generoi_alkuluvut(1024)
        self.assertEqual(alkuluvut[0], 170141183460469231731687303715884105727)
        self.assertNotEqual(alkuluvut[1], 170141183460469231731687303715884105727)
        self.assertEqual(alkuluvut[1], 162259276829213363391578010288127)

    def test_parillinen_luku(self):
        fake_random = StubRandomBits()
        primes = AlkulukuGeneraattori(fake_random)
        fake_random.lisaa_getrandbits([170141183460469231731687303715884105722, 170141183460469231731687303715884105720, 162259276829213363391578010288127, 4704696367753654905950376252200829949138702499452617714632570448046245636338838115623091484174563253076891246859772084383591873610634282045310638869311537])
        alkuluvut = primes.generoi_alkuluvut(1024)
        self.assertEqual(alkuluvut[0], 162259276829213363391578010288127)
        self.assertEqual(alkuluvut[1], 4704696367753654905950376252200829949138702499452617714632570448046245636338838115623091484174563253076891246859772084383591873610634282045310638869311537)

    def test_avaimella_oikea_pituus_1024(self):
        p, q = self.primes.generoi_alkuluvut(1024)
        n = p*q
        self.assertGreater(len(bin(n)[2:]), 1000)

    def test_avaimella_oikea_pituus_2048(self):
        p, q = self.primes.generoi_alkuluvut(2048)
        n = p*q
        self.assertGreater(len(bin(n)[2:]), 2000)

    def test_avaimella_oikea_pituus_4096(self):
        p, q = self.primes.generoi_alkuluvut(4096)
        n = p*q
        self.assertGreater(len(bin(n)[2:]), 4000)
