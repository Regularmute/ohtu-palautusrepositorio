import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "pulla", 7)
            if tuote_id == 3:
                return Tuote(3, "kolibri", 200)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock,
                        self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pete", "33333")

        self.pankki_mock.tilisiirto.assert_called_with("pete", ANY, "33333", ANY, 5)

    def test_kahden_eri_tuotteen_osto_kutsuu_pankin_metodia_tilisiirto_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("jooseppi", "11122")

        self.pankki_mock.tilisiirto.assert_called_with("jooseppi", ANY, "11122", ANY, 12)

    def test_kahden_saman_tuotteen_osto_kutsuu_pankin_metodia_tilisiirto_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("kalevi", "99223")

        self.pankki_mock.tilisiirto.assert_called_with("kalevi", ANY, "99223", ANY, 10)

    def test_loppuneen_tuotteen_osto_ei_vaikuta_toiseen_oston_summaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("sabrina", "55123")

        self.pankki_mock.tilisiirto.assert_called_with("sabrina", ANY, "55123", ANY, 7)

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_hinnan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("kaarina", "88111")

        self.pankki_mock.tilisiirto.assert_called_with("kaarina", ANY, "88111", ANY, 5)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("kaarina", "88111")

        self.pankki_mock.tilisiirto.assert_called_with("kaarina", ANY, "88111", ANY, 7)
