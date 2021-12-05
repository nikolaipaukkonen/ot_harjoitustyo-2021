''' Luokka stratigrafisille yksiköille '''

class Locus:
    def __init__(self, l_type, name, descr, thick, above):
        self.l_type=l_type
        self.name=name
        self.descr=descr
        self.thick=thick
        self.above=above
