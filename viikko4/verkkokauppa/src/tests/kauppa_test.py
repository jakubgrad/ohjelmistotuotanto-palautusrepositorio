import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    #Let's start the transaction, add a product that is in stock to the basket and make the purchase, i.e. 
    #call the method of purchase tilimaksu, make sure that the bank's method is called tilisiirtowith the 
    #correct customer, account numbers and amount. This is otherwise a copypaste from the example, but 
    #assert_called_withthe -method should be used in order to check that the parameters have the correct values
    def test_tilisiirto_is_called_with_the_correct_customer_account_numbers_and_amount(self):
            pankki_mock = Mock()
            viitegeneraattori_mock = Mock()

            # palautetaan aina arvo 42
            viitegeneraattori_mock.uusi.return_value = 42

            varasto_mock = Mock()

            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10

            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)

            # otetaan toteutukset käyttöön
            varasto_mock.saldo.side_effect = varasto_saldo
            varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            kauppa.lisaa_koriin(1)
            kauppa.tilimaksu("pekka", "12345")

            # varmistetaan, että metodia tilisiirto on kutsuttu with correct arguments
            pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
            #nimi, viitenumero, tililta, tilille, summa
            


    #Let's start the transaction, add two different products that are in stock to the basket and make the purchase, 
    #make sure that the bank's method is called tilisiirtowith the correct customer, account number and amount
    def test_tilisiirto_is_called_with_the_correct_customer_account_numbers_and_amount_for_two_different_products(self):
            pankki_mock = Mock()
            viitegeneraattori_mock = Mock()

            # palautetaan aina arvo 42
            viitegeneraattori_mock.uusi.return_value = 42

            varasto_mock = Mock()

            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10
                if tuote_id == 2:
                    return 20

            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)
                if tuote_id == 2:
                    return Tuote(2, "cream", 3)

            # otetaan toteutukset käyttöön
            varasto_mock.saldo.side_effect = varasto_saldo
            varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            kauppa.lisaa_koriin(1)
            kauppa.lisaa_koriin(2)
            kauppa.tilimaksu("pekka", "12345")

            # varmistetaan, että metodia tilisiirto on kutsuttu with correct arguments
            pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

        #Let's start the transaction, add two of the same products to the basket , of which there is enough 
        #in stock and make the purchase, make sure that the bank's method is called tilisiirtowith the correct 
        #customer, account number and amount
    def test_tilisiirto_is_called_with_the_correct_customer_account_numbers_and_amount_for_the_same_product_twice(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        
        #adding two of the same product
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu with correct arguments
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

        #Let's start the transaction, add a product that is enough in stock and a product that
        #is out of stock to the basket and make the purchase, make sure that the bank's method 
        #is called tilisiirtowith the correct customer, account number and amount
    def test_tilisiirto_is_called_correctly_for_product_that_is_missing_and_one_that_is_enough(self):
            pankki_mock = Mock()
            viitegeneraattori_mock = Mock()

            # palautetaan aina arvo 42
            viitegeneraattori_mock.uusi.return_value = 42

            varasto_mock = Mock()

            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10
                if tuote_id == 2:
                    return 0

            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)
                if tuote_id == 2:
                    return Tuote(2, "cream", 3)

            # otetaan toteutukset käyttöön
            varasto_mock.saldo.side_effect = varasto_saldo
            varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            
            #adding two of the same product
            kauppa.lisaa_koriin(1)
            kauppa.lisaa_koriin(2)
            kauppa.tilimaksu("pekka", "12345")

            # varmistetaan, että metodia tilisiirto on kutsuttu with correct arguments
            pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_aloita_asiointi_resets_the_data_of_the_previous_purchase(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        
        self.assertEqual(kauppa._ostoskori.hinta(), 5)
        
        kauppa.aloita_asiointi()

        self.assertEqual(kauppa._ostoskori.hinta(), 0)