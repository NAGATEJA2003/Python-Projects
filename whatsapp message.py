import os
import time
import webbrowser
from datetime import datetime
from string import ascii_letters

name = input('Enter the contact number of a person you want to send message in WhatsApp: ')
message = input('Enter the message:\n')
time1 = input('Enter time in {hh:mm:ss} format: ')

# Check if there aren't any ':' in the input time
if ":" not in time1:
    print("Please input a correct time format")
    os._exit(0)
# Check if there are any letters in the input time
elif ascii_letters in time1:
    print("Please input a correct time format")
    os._exit(0)

print(f'Time entered by user: {time1}')

# Check every .9 seconds if the current time is the same as the user input time
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f'Current time: {current_time}')

    if time1 == current_time:
        webbrowser.open(f'https://web.whatsapp.com/send?phone=+91{name}&text={message}', new=0)
        break
    else:
        time.sleep(0.9)
