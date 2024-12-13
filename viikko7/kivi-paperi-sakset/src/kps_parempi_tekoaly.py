from game import Game
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(Game):
    def __init__(self):
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)

    def game_specific(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        if not self._onko_ok_siirto(ekan_siirto):
            return False

        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")

        self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
        self.tekoaly.aseta_siirto(ekan_siirto)
        return True
