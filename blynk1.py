BLYNK_TEMPLATE_ID = "TMPL4x7d2JJMM"
BLYNK_TEMPLATE_NAME = "IoT RPi 4"
BLYNK_AUTH_TOKEN = "y5Z9Uu7f9Q2of4OjX1tRjlgv35m8eC3-"

import requests  # Library for sending requests to the Blynk REST API
from time import sleep
import sys
#from sense_emu import SenseHat  # Use this line if running on a Sense Hat emulator
from sense_hat import SenseHat  # Use this line if running on a physical Sense Hat

AUTH_TOKEN = BLYNK_AUTH_TOKEN

s = SenseHat()
count = 1

try:
    while count <= 10:  # Exactly 10 iterations
        temp = round(s.get_temperature(), 1)  # Get temperature rounded to one decimal place
        humid = round(s.get_humidity(), 1)  # Get humidity rounded to one decimal place
        print(f"Temperature: {temp} °C")
        print(f"Humidity: {humid} %")

        # Create the URL with the sensor values to send to Blynk
        url = f"https://blynk.cloud/external/api/batch/update?token={AUTH_TOKEN}&V1={temp}&V2={humid}"

        response = requests.get(url)  # Send the request to Blynk
        if response.status_code == 200:
            print(f"Request #{count} successfully sent to Blynk")
        else:
            print("Error:", response.status_code, response.text)
        count += 1
        if count <= 10:
            sleep(5)  # Wait 5 seconds before sending the next set of data
    print("Finished: sent 10 iterations.")
except KeyboardInterrupt:
    print('\b\bExiting...')
    sys.exit(0)
except Exception as e:
    print("Exception:", e)