import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(400)
        self.kassapaate = Kassapaate()
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def test_edullinen_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(str(self.kassassa_rahaa), "100240")
        self.assertEqual(self.edulliset, 1)

    def test_edullinen_kateisella_eponnistuu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassassa_rahaa), "100000")
        self.assertEqual(self.edulliset, 0)

    def test_maukas_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(str(self.kassassa_rahaa), "100450")
        self.assertEqual(self.maukkaat, 1)

    def test_maukas_kateisella_eponnistuu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(str(self.kassassa_rahaa), "100000")
        self.assertEqual(self.maukkaat, 0)

    def test_edullisesti_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.6")
        self.assertEqual(self.edulliset, 1)
        self.assertEqual(str(self.kassassa_rahaa), "100000")

    def test_edullisesti_kortilla_eponnistuu(self):
        self.kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 0.1")
        self.assertEqual(self.edulliset, 0)
        self.assertEqual(str(self.kassassa_rahaa), "100000")

    def test_maukkaasti_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
        self.assertEqual(self.maukkaat, 1)
        self.assertEqual(str(self.kassassa_rahaa), "100000")

    def test_maukkaasti_kortilla_eponnistuu(self):
        self.kortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "saldo: 0.1")
        self.assertEqual(self.maukkaat, 0)
        self.assertEqual(str(self.kassassa_rahaa), "100000")

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
        self.assertEqual(str(self.kassassa_rahaa), "100100")

    def test_ei_lataa_negatiivista_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "saldo: 4.0")
        self.assertEqual(str(self.kassassa_rahaa), "100000")
