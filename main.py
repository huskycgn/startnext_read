from funcs import get_startnext_amount, send_message, run_program
from time import sleep

# print(startvalue)
while True:
    try:
        run_program()
        sleep(30)
    except AttributeError:
        continue
