import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):

    ### Testien alustus ja alkutilanne ###

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_rahamaara_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myydyt_edulliset_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myydyt_maukkaat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    ### Kateismyynnin testit ###

    def test_kateisosto_edullisella_kassan_rahamaara_kasvaa_kun_maksu_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_edullisella_vaihtoraha_oikein_kun_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_kateisosto_edullisella_myytyjen_maara_kasvaa_kun_maksu_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_edullisella_kassan_rahamaara_ei_muutu_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_edullisella_kaikki_rahat_palautetaan_kun_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_kateisosto_edullisella_myytyjen_maara_ei_muutu_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukkaasti_kassan_rahamaara_kasvaa_kun_maksu_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_maukkaasti_vaihtoraha_oikein_kun_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kateisosto_maukkaasti_myytyjen_maara_kasvaa_kun_maksu_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_maukkaasti_kassan_rahamaara_ei_muutu_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_maukkaasti_kaikki_rahat_palautetaan_kun_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_kateisosto_maukkaasti_myytyjen_maara_ei_muutu_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    ### Korttimyynnin testit ###

    def test_edullisesti_jos_kortilla_tarpeeksi_rahaa_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        
    def test_edullisesti_jos_kortilla_tarpeeksi_rahaa_veloitetaan_summa_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_edullisesti_jos_kortilla_tarpeeksi_rahaa_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_jos_kortilla_tarpeeksi_rahaa_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) 
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisesti_jos_kortilla_ei_tarpeeksi_rahaa_palautetaan_false(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_edullisesti_jos_kortilla_ei_tarpeeksi_rahaa_kortin_raha_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_edullisesti_jos_kortilla_ei_tarpeeksi_rahaa_myytyjen_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisesti_jos_kortilla_ei_tarpeeksi_rahaa_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaasti_jos_kortilla_tarpeeksi_rahaa_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        
    def test_maukkaasti_jos_kortilla_tarpeeksi_rahaa_veloitetaan_summa_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_maukkaasti_jos_kortilla_tarpeeksi_rahaa_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_jos_kortilla_tarpeeksi_rahaa_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) 
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaasti_jos_kortilla_ei_tarpeeksi_rahaa_palautetaan_false(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_maukkaasti_jos_kortilla_ei_tarpeeksi_rahaa_kortin_raha_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_maukkaasti_jos_kortilla_ei_tarpeeksi_rahaa_myytyjen_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_maukkaasti_jos_kortilla_ei_tarpeeksi_rahaa_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    ### Rahan lataaminen ###

    def test_kortin_lataamisessa_kortin_rahamaara_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.maksukortti.saldo, 1200)

    def test_kortin_lataamisessa_kassan_rahamaara_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_kortin_lataamisessa_negatiivinen_arvo_ei_muuta_korttisaldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_kortin_lataamisessa_negatiivinen_arvo_ei_muuta_kassasaldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)