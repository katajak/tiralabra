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
        """Metodi, joka lukee käyttäjän syötteen inquirer moduulilla.
        Metodille annetaan syötteenä kysymys, joka näytetään käyttäjälle.
        """
        nimi = "syote"
        kysymys = inquirer.Text(nimi, message=syote),

        vastaus = inquirer.prompt(kysymys)
        return vastaus[nimi]

    def lue_lista(self, viesti, valinnat):
        """Metodi, joka lukee käyttäjän syötteen inquirer moduulilla (lista).
        Metodille annetaan syötteenä kysymys, joka näytetään käyttäjälle,
        sekä listassa valinnat jotka ovat käyttäjän valittavissa.
        """
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
                "selection_color": "bright_yellow",
                "selection_cursor": "->"
            }
        }

        vastaus = inquirer.prompt(kysymys, theme=load_theme_from_dict(teema))
        return vastaus[nimi]
