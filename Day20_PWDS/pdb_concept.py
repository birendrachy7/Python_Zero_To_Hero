# PDB commands:

import pdb

def complex_function(a,b):
    result = a*b
    pdb.set_trace()
    c=20
    if result>50:
        pdb.set_trace()
        return "Large Result"
    return "Small result"


complex_function(10,7)