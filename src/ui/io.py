import inquirer
from inquirer.themes import load_theme_from_dict


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

        teema = {
            "List": {
                "selection_color": "gold",
                "selection_cursor": "->"
            }
        }

        prompt = inquirer.prompt(questions, theme=load_theme_from_dict(teema))
        return prompt[nimi]
