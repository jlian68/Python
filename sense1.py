from sense_hat import SenseHat
import time

s = SenseHat()

s.low_light = True

s.show_letter("f",text_colour=(0,255,0))

time.sleep(10)

s.clear()




