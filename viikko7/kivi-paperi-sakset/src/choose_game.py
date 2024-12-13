from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def ChooseGame(vastaus):
    game_modes = {
            'a': KPSPelaajaVsPelaaja(),
            'b': KPSTekoaly(),
            'c': KPSParempiTekoaly()
        }
    if vastaus in game_modes:
        return game_modes[vastaus]