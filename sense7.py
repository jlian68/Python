from sense_emu import SenseHat
from time import sleep
s = SenseHat()
s.low_light=True

# Ορίζουμε τις συναρτήσεις:
def pano():
  s.show_letter('P')

def kato():
  s.show_letter('K')

def aristero():
  s.show_letter('A')
  
def deksi():
  s.show_letter('D')

while True:
    s.stick.direction_up = pano
    s.stick.direction_down = kato
    s.stick.direction_left = aristero
    s.stick.direction_right = deksi
    # με το μεσαίο κουμπί εκτελείται η μέθοδος s.clear
    s.stick.direction_middle = s.clear
    sleep(0.1)