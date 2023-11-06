


DataReadout
    - displaydata ()


Vat
    {'chemical': str, 
    - volume (float)
    }


Door
    - location (str)
    - dangerRating (int)s


DataInterface
    - dictionary of N types of items (currently Vats and Doors); 
    {'vats': [[vat1, stateOfvat1 ], ...]. 
       'doors': [door1, door2, ...]}
    

VatState (class):
    - temperature (float)

DataEvents
    - 