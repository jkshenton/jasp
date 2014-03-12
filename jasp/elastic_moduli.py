import numpy as np
from jasp import *

def get_elastic_moduli(self):
    '''returns the total elastic moduli in GPa (i.e. the rigid ion and
    contributions from relaxation) from the OUTCAR file.

    you must run with IBRION=6 and ISIF>= 3 for this output to exist.

    There are also contributions from ionic relaxation
     ELASTIC MODULI CONTR FROM IONIC RELAXATION (kBar)
     and the rigid moduli
     SYMMETRIZED ELASTIC MODULI (kBar)

     For now these are not returned.
    '''
    self.calculate()
    
    with open('OUTCAR') as f:
        lines = f.readlines()

    TEM = []
    for i, line in enumerate(lines):
        if line.startswith(' TOTAL ELASTIC MODULI (kBar)'):
            j = i + 3
            data = lines[j:j+6]
            break

    for line in data:
        # each line looks like this:
        # XX        2803.5081   1622.6085   1622.6085      0.0000      0.0000      0.0000
        TEM += [[float(x) for x in line.split()[1:]]]

    return np.array(TEM) * 0.1 # (convert to GPa)

Vasp.get_elastic_moduli = get_elastic_moduli
