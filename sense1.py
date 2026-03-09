from sense_hat import SenseHat
s = SenseHat()
s.low_light=True

# Με την clear() σβήνουμε τυχόν παλιές τιμές
# που έχει δεχθεί η LED συστοιχία
s.clear()

# Αποθηκεύουμε τις τιμές των αισθητήρων θερμοκρασίας,
# υγρασίας και ατμοσφαιρικής πίεσης στις μεταβλητές
# temp, humid και pressure αντίστοιχα.
temp = s.temperature
humid = s.humidity
pressure = s.pressure

# στρογγυλοποιούμε τις παραπάνω τιμές στο πρώτο δεκαδικό:
temp = round(temp,1)
humid = round(humid,1)
pressure= round(pressure,1)

# Εκτυπώνουμε τις τιμές στην κονσόλα
# προσθέτοντας στο τέλος και τις μονάδες:
print("Θερμοκρασία: ", temp, "C")
print("Υγρασία: ", humid,"%")
print("Ατμοσφαιρική πίεση: ", pressure, "mbar")

# Εμφανίζουμε τις τιμές στη συστοιχία LED:
s.show_message("Temp:"+str(temp)+"C")
s.show_message("Humid:"+str(humid)+"%")
s.show_message("Pressure:"+str(pressure)+"mbar")




