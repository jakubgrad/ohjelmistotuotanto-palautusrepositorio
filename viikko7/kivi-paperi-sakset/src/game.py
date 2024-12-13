from tuomari import Tuomari

class Game:
    def __init__(self):
        self.tuomari = Tuomari()

    def pelaa(self):
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        
        while self.game_specific():
            print(self.tuomari)

        print("Kiitos!")
        print(self.tuomari)
    
    def game_specific(self):
        return 0

    def _onko_ok_siirto(self, siirto):
        return siirto in ["k","p","s"]