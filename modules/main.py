# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this
import time
import math
import datetime
import sys
from greet import supergreeting

def wait(seconds: int):
    time.sleep(seconds)
    return

def my_sin(number: float):
    sin_of_number = math.sin(number)
    return sin_of_number

def iso_now():
    date = datetime.datetime.now().replace(microsecond=0).isoformat()
    return date

def platform():
    platform = sys.platform
    return platform

def supergreeting_wrapper(name: str):
    greeting = supergreeting(name)
    return greeting

print(wait(5))
print(my_sin(5.7))
print(iso_now())
print(platform())
print(supergreeting_wrapper("Jochum"))
