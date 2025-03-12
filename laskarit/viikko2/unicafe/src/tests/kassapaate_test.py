import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_luodun_kassapaatteen_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
    def test_luodun_kassapaatteen_myydyt_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_luodun_kassapaatteen_myydyt_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

# käteistestit alkaa tästä

    def test_kateisosto_edullisesti_riittava_maksu_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_kateisosto_edullisesti_riittava_maksu_palauttaa_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
    
    def test_kateisosto_edullisesti_riittava_maksu_lisaa_myytyja_edullisia(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_edullisesti_maksu_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_edullisesti_ei_riittava_maksu_palauttaa_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(239), 239)
    
    def test_kateisosto_edullisesti_ei_riittava_maksu_ei_lisaa_myytyja_edullisia(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_maukkaasti_riittava_maksu_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_kateisosto_maukkaasti_riittava_maksu_palauttaa_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)

    def test_kateisosto_maukkaasti_riittava_maksu_lisaa_myytyja_maukkaita(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_maukkaasti_maksu_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_maukkaasti_ei_riittava_maksu_palauttaa_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(399), 399)
    
    def test_kateisosto_maukkaasti_ei_riittava_maksu_ei_lisaa_myytyja_maukkaita(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.maukkaat, 0)

# korttitestit alkaa tästä
    
    def test_korttiosto_edullisesti_riittava_saldo_veloitetaan(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.60)
    
    def test_korttiosto_edullisesti_riittava_saldo_toimii(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
    
    def test_korttiosto_edullisesti_riittava_saldo_kasvattaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.60)