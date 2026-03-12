from sense_hat import SenseHat
from time import sleep
import sys

s = SenseHat()
s.low_light=True

# Ορίζουμε τις συναρτήσεις:
def up():
  s.show_letter('U')

def down():
  s.show_letter('D')

def left():
  s.show_letter('L')
  
def right():
  s.show_letter('R')

try:
    while True:
        s.stick.direction_up = up
        s.stick.direction_down = down
        s.stick.direction_left = left
        s.stick.direction_right = right
        # με το μεσαίο κουμπί εκτελείται η μέθοδος s.clear
        s.stick.direction_middle = s.clear
        sleep(0.1)
except KeyboardInterrupt:
    s.clear()
    print('\b\bExiting...')
    sys.exit(0)