''' Luokka stratigrafisille yksiköille '''

class Locus:
    ''' Luokka, joka kuvaa stratigrafista kerrosta tai kontekstia (locusta).

    Attributes:
        l_type: Locuksen tyyppi (maakerros, rakenne tai leikkaus).
        name: Locuksen uniikki nimi.
        descr: Locuksen sanallinen kuvaus.
        thick: Locuksen paksuus senttimetreinä.
        above: Mahdollisen ylläolevan locuksen id.
        '''

    def __init__(self, l_type, name, descr, thick, above):
        ''' Konstruktori, jolla luodaan uusi locus.

        Args:
            l_type: Locuksen tyyppi (maakerros, rakenne tai leikkaus).
            name: Locuksen uniikki nimi.
            descr: Locuksen sanallinen kuvaus.
            thick: Locuksen paksuus senttimetreinä.
            above: Mahdollisen ylläolevan locuksen id.
        '''

        self.l_type=l_type
        self.name=name
        self.descr=descr
        self.thick=thick
        self.above=above
