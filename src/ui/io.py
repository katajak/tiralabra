import inquirer
from inquirer.themes import load_theme_from_dict


class IO:
    """Luokka, joka on vastuussa käyttäjän syötteiden lukemisesta
       ja näytölle kirjoittamisesta.
    """
    def kirjoita(self, syote):
        print(syote)

    def lue(self, syote):
        return input(syote)

    def lue_lyhyt(self, syote):
        nimi = "syote"
        kysymys = inquirer.Text(nimi, message=syote),

        vastaus = inquirer.prompt(kysymys)
        return vastaus[nimi]

    def lue_lista(self, viesti, valinnat):
        nimi = "syote"
        kysymys = [
            inquirer.List(
                nimi,
                message=viesti,
                choices=valinnat,
                carousel=True,
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
