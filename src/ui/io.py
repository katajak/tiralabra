import inquirer
from inquirer.themes import GreenPassion


class IO:
    """Luokka, joka toimii kuten print ja input.
    """
    def lue(self, syote):
        return input(syote)

    def kirjoita(self, syote):
        print(syote)

    def lue_lista(self, nimi, viesti, valinnat):
        questions = [
            inquirer.List(
                nimi,
                message=viesti,
                choices=valinnat,
            ),
        ]

        return inquirer.prompt(questions, theme=GreenPassion())
