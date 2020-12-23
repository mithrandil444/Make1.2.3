#!/usr/bin/env python
"""
This is a Python script that will display the lyrics of a song
"""

# IMPORTS


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Finished"


# CONFIGURING I/O


def main():
    class Song:                         # Define class Song
        def __init__(self, lyrics):
            self.lyrics = lyrics        # Deifine lyrics

        def sing(self):                 # Define the song (de_aarde)
            return de_aarde.lyrics      # Return the song

    de_aarde = Song("""De aarde is een grote bol
Met planten en met beestjes vol
En ze draait al heel lang in het rond
En wat ik haast niet kan geloven
Soms lopen we ondersteboven
En toch lijven onze voeten op de grond
En al de wolkjes boven ons
Die lijken wel 1 grote spons
Ze brengen ons de water van de zee
En als de aarde drinken wil
Dan haalt de wind de wolkjes stil
En dan valt al dat water naar beneeeee

Oooh grote wereldbol, ik snap er niet veel van
Het is gewoon een wonder wat je allemaal kan
Je vliegt maar, je vliegt maar zonder te verdwalen
Je draait maar en je draait maar zonder moter of bedalen

Als de zand dan weer verdwijnt
En de zon haar zonnenstraaltjuh schijnt
Lekker op de rug van onze poes
Dan valt aan de andere kant de nacht
Daarist janneke maan die lacht
Naar de ingeslapen kangoeroes!
En als jezuke zijn bedje maakt
En al zijn pluimjes kwijt geraakt
Dan begind het hier bij ons te sneeuwen
Toch brand de zon in afrika
De negertjes tot chocola
Maar bijt ze niet want anders gaan ze schreeuwen

En van waar dit allemaal komt:
De lucht, het water en de grond
Dat kan tot nu toe niemand vertellen
De aarde draait hier niet alleen
Er zijn nog meer bollen om haar heen
Veel meer dan de mensen kunnen tellen
Want als je straks een lichtje ziet
Dat plotseling door de hemel schiet
Dan kan dat een marsmannetje zijn
Da heel gewoon aan jou komt vragen
Of je een van deze dagen
Met hem mee vliegt in zijn mars konijn""")
    print(de_aarde.lyrics)                  # Print the song

if __name__ == '__main__':  # code to execute if called from command-line
    main()
