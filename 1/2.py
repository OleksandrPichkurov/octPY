'''
import os
import sys
import django
print(django.VERSION)
sys.path.append('/home/sol/hill')
print(sys.path)
#from module import *
#from module2 import *
#from module import calc_total_price
from fmodule import module
#import module2
'''
#from module import calc_total_price
import module as ss

print(dir())
z = ss.calc_total_price(price=123, discount=2, z=123)

