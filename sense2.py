from sense_emu import SenseHat
from time import sleep
s = SenseHat()

# O Βρόχος while True θα εκτελείται μέχρι να διακόψουμε το πρόγραμμά μας.
while True:
    # Το sense-Hat επιστρέφει ένα λεξικό, που είναι μια 
    # δομή δεδομένων στην python και  περιλαμβάνει τους τίτλους
    # των τριών αξόνων μαζί με τις τιμές τους
    orient = s.orientation
#    print(orient)    
    x, y, z = orient['roll'], orient['pitch'], orient['yaw']
    print(round(x, 3), round(y, 3), round(z, 3))
    # προσθέτουμε μια μικρή παύση 0.1 του δευτερολέπτου στην επανάληψη του βρόχου
    sleep(0.1)