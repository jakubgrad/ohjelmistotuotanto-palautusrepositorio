from game import Game
from tuomari import Tuomari


class KPSPelaajaVsPelaaja(Game):
    def game_specific(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = input("Toisen pelaajan siirto: ")
        if not self._onko_ok_siirto(ekan_siirto) or not self._onko_ok_siirto(tokan_siirto): 
            return False
        self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
        return True