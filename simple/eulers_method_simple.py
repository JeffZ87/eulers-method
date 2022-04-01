"""Application of Euler's method in python"""

import datetime
import time


def euler_function(x_val: float, y_val: float, step_size: float, target_x: float) -> float:
    """The euler_function applies the euler method until the target x value is reached."""
    while x_val < target_x:
        y_val = y_val + (diff_eq_val(x_val, y_val) * step_size)
        x_val = round(x_val + step_size, 2)

    return y_val
    

def diff_eq_val (x: float, y: float) -> float:
    """Contains the differential equation; takes x & y as paramater and return decimal value of differential equation."""
    return x ** 2 + y ** 2


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


start_time = time.time()
print(f"Start at: {datetime.datetime.now()}")

# initialize information needed for Euler's evaluation 
step_size: float = 0.1
x_init: float = 0
y_init: float = 0
target1: float = 1
target2: float = 2
target3: float = 3

print(euler_function(x_init, y_init, step_size, target1))
print(euler_function(x_init, y_init, step_size, target2))
print(euler_function(x_init, y_init, step_size, target3))

end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)