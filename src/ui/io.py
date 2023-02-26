class IO:
    """Luokka, joka toimii kuten print ja input.
    """
    def lue(self, syote):
        return input(syote)

    def kirjoita(self, syote):
        print(syote)
