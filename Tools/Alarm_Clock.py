
"""A simple alarm clock that plays a sound when the time is met.

Sound from https://freesound.org/people/MATRIXXX_/sounds/453137/
This work is licensed under the Creative Commons 0 License.

"""

from datetime import datetime
import time
import subprocess

def now():
    """Get the current time (HH:MM)"""
    return datetime.now().time().strftime("%H:%M") # time object


def play_sound():
    """Play the sound"""
    subprocess.call(['afplay', '453137__matrixxx__robot-no.wav'])


print("now =", now())
print('Make sure volume is up')
play_sound()
play_sound()

while True:
    alarm = input('Enter designated time (HH:MM) or exit: ')
    if now() <= alarm:
        print(f'Alarm set for {alarm}')
        break
    elif alarm == 'exit':
        break
    else:
        print('invalid entry')

while True:
    time.sleep(5)
    if now() >= alarm:
        print('ALARM')
        play_sound()
        play_sound()
        break
    else:
        print(f'Alarm set for {alarm}, it is now {now()}')

