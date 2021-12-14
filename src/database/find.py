''' Luokka löydöille '''

class Find:
    ''' Luokka, joka kuvaa arkeologisesta kontekstista tehtyä löytöä.
    
    Attributes: 
        find_type: Löydön tyyppi.
        dating: Löydön ajoitus periodina.
        descr: Löydön sanallinen kuvaus.
        weight: Löydön paino grammoina.
        locus: Stratigrafinen yksikkö (locus), jossa löytö on tehty.
        '''
    
    def __init__(self, find_type, dating, descr, weight, locus):
        ''' Luokan konstruktori, jolla luodaan uusi löytö.
        
        Args:
            find_type: Löydön tyyppi.
            dating: Löydön ajoitus periodina.
            descr: Löydön sanallinen kuvaus.
            weight: Löydön paino grammoina.
            locus: Stratigrafinen yksikkö (locus), jossa löytö on tehty.
        '''
        
        self.find_type=find_type
        self.dating=dating
        self.descr=descr
        self.weight=weight
        self.locus=locus
        
