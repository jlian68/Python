# Εισαγωγή της βιβλιοθήκης για διαχείριση του Sense HAT
from sense_hat import SenseHat
# Εισαγωγή της βιβλιοθήκης για διαχείριση του χρόνου
import time

# Δημιουργία της μεταβλητής-αντικειμένου s για επικοινωνία με το Sense HAT
s = SenseHat()
s.clear()
s.low_light=True
s.set_imu_config(True, True, True)

# Εναλλαγή μηνυμάτων LED ανά επανάληψη ώστε να μη μπλοκάρει για πολλή ώρα
led_message_index = 0

try:
   # Επανάληψη εργασιών για πάντα
   while True:
      # Διάβασμα της θερμοκρασίας και απόδοση στη μεταβλητή temp
      temp = s.get_temperature()
   
      # Διάβασμα της υγρασίας και απόδοση στη μεταβλητή humid
      humid = s.get_humidity()
   
      # Διάβασμα της πίεσης και απόδοση στη μεταβλητή press
      press = s.get_pressure()
   
      # Διάβασμα του προσανατολισμού και απόδοση στη μεταβλητή orient
      orient = s.get_orientation_degrees()
   
      # Διάβασμα της βαρυτικής επιτάχυνσης και απόδοση στη μεταβλητή accel
      accel = s.get_accelerometer_raw()
   
      # Εμφάνιση των μεταβλητών στην κονσόλα
      print('Θερμοκρασία (°C): ' + str(round(temp, 1)))
      print('Υγρασία (%).....: ' + str(round(humid, 1)))
      print('Πίεση (mbar)....: ' + str(round(press, 1)))
      print('Προσανατολισμός')
      print('   roll (°).....: ' + str(round(orient['roll'], 1)))
      print('   pitch (°)....: ' + str(round(orient['pitch'], 1)))
      print('   yaw (°)......: ' + str(round(orient['yaw'], 1)))
      print('Βαρυτική επιτάχυνση')
      print('   x (g).........: ' + str(round(accel['x'], 1)))
      print('   y (g).........: ' + str(round(accel['y'], 1)))
      print('   z (g).........: ' + str(round(accel['z'], 1)))
      print('Τα δεδομένα εμφανίζονται και στη συστοιχία LED του Sense HAT...')
      print()
   
      # Εμφάνιση ενός μόνο μηνύματος ανά κύκλο για συχνότερη ανανέωση μετρήσεων
      led_messages = [
         'Temp (C): ' + str(round(temp, 1)),
         'Hum (%): ' + str(round(humid, 1)),
         'Pres (mbar): ' + str(round(press, 1)),
         'Roll: ' + str(round(orient['roll'], 1)),
         'Pitch: ' + str(round(orient['pitch'], 1)),
         'Yaw: ' + str(round(orient['yaw'], 1)),
         'x (g): ' + str(round(accel['x'], 2)),
         'y (g): ' + str(round(accel['y'], 2)),
         'z (g): ' + str(round(accel['z'], 2)),
      ]
      s.show_message(led_messages[led_message_index], scroll_speed=0.05)
      led_message_index = (led_message_index + 1) % len(led_messages)
   
      # Καθυστέρηση μέχρι την επόμενη επανάληψη (σε δευτερόλεπτα)
      time.sleep(0.5)
      s.clear()
except KeyboardInterrupt:
   print('\nΤερματισμός με Ctrl+C...')
finally:
   s.clear()
