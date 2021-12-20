''' Luokka erilaisille näytteille '''

class Sample:
    ''' Luokka, joka kuvaa arkeologisesta kontekstista otettua näytettä

    Attributes:
        sample_type: Näytteen tyyppi (hiili-, maaperä- tai muu näyte)
        sample_locus: Yksikkö, josta näyte otettiin.
        '''

    def __init__(self, sample_type, sample_locus):
        ''' Luokan konstruktori, jolla luodaan uusi näyte.

        Args:
        sample_type: Näytteen tyyppi (hiili-, maaperä- tai muu näyte)
        sample_locus: Yksikkö, josta näyte otettiin.
        '''

        self.sample_type = sample_type
        self.sample_locus = sample_locus
