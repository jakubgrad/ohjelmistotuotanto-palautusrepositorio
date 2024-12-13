from choose_game import ChooseGame

def main():
    while True:
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

        vastaus = input()
        game = ChooseGame(vastaus)
        if game is not None:
            game.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
