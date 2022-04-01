"""Application of Euler's method in python"""

from decimal import *
from fractions import *
import datetime
import time

def euler_function(x_val, y_val, step_size, target_x) -> Fraction:
    """The euler_function applies the euler method until the target x value is reached."""
    while x_val < target_x:
        print(f"Start euler_function.y_val calculation and loop: {datetime.datetime.now()}")
        y_val = (y_val + (diff_eq_val(x_val, y_val) * step_size)).limit_denominator(1000)

        # print(y_val)
        x_val = x_val + step_size
        print(f"\n\nAt x_val {x_val}\n\n")
    return y_val.limit_denominator(1000)

def diff_eq_val (x, y) -> Fraction:
    """Contains the differential equation; takes x & y as paramater and return decimal value of differential equation."""
    print(f"diff_eq_val call: {datetime.datetime.now()}")

    # x = round(x, 18)
    # y = round(y, 18)
    # x = Fraction(x).limit_denominator(1000)
    # y = Fraction(y).limit_denominator(1000)
    # x
    # return round(x ** 2, 10) + round(y ** 2, 10)
    print(f"Start diff_eq_val calculation: {datetime.datetime.now()}")
    return (x ** 2 + y ** 2).limit_denominator(1000)

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

start_time = time.time()

print(f"Start at: {datetime.datetime.now()}")
# initialize information needed for Euler's evaluation 
step_size = Fraction(0.01).limit_denominator(1000)
x_init = Fraction(0)
y_init = Fraction(0)
target1 = Fraction(1)
target2 = Fraction(2)
target3 = Fraction(3)
# getcontext().prec = 999999
# getcontext().Emax = MAX_EMAX
# print(euler_function(x_init, y_init, step_size, target1))
# print(euler_function(x_init, y_init, step_size, target2))
print(euler_function(x_init, y_init, step_size, target3))
# print(getcontext())
# print(type(step_size))

end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)