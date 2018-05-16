# This application supports operation of a Philips Hue smart bulb using Python

from phue import Bridge
from time import sleep

IP = "192.168.1.168"        # Ip address of the Philips Hue bridge
b = Bridge(IP)              # Instance of Bridge class


def connect(b):
    # If the app is not registered and the button is not pressed, press the button and call connect()
    # (this only needs to be run a single time)
    b.connect()
    b.get_api()     # Get the bridge state (This returns the full dictionary that you can explore)


def list_bulbs(b):
    lights = b.lights
    for l in lights:        # Print list of light names
        print(l.name)
    return lights


def set_params(light_ID, param, value):
    # Example b.set_light(2,'on', True), b.set_light(2, 'bri', 200)
    b.set_light(light_ID, param, value)


# Operating the Hue bulb
connect(b)      # connecting to the Huw bulb
bulbs = list_bulbs(b)   # listing available bulbs
set_params(bulbs[0], 'on', True)        # changing bulb parameters  - Switching ON
sleep(4)
set_params(bulbs[0], 'bri', 200)        # changing bulb parameters - Adjust brightness
sleep(4)
set_params(bulbs[0], 'on', False)       # changing bulb parameters - Switching OFF
