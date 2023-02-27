import inquirer
from inquirer.themes import load_theme_from_dict


class IO:
    """Luokka, joka on vastuussa käyttäjän syötteiden lukemisesta
       ja näytölle kirjoittamisesta.
    """
    def lue(self, syote):
        return input(syote)

    def kirjoita(self, syote):
        print(syote)

    def lue_lista(self, viesti, valinnat):
        nimi = "syote"
        kysymys = [
            inquirer.List(
                nimi,
                message=viesti,
                choices=valinnat,
            ),
        ]

        teema = {
            "List": {
                "selection_color": "gold",
                "selection_cursor": "->"
            }
        }

        vastaus = inquirer.prompt(kysymys, theme=load_theme_from_dict(teema))
        return vastaus[nimi]
