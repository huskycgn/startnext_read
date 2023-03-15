from funcs import get_startnext_amount, send_message
from time import sleep
from datetime import datetime

startvalue = get_startnext_amount()
print(startvalue)
while True:
    newvalue = get_startnext_amount()
    if newvalue != startvalue:
        send_message(f'Betrag ist jetzt {newvalue} €')
    print(datetime.now())
    print(f'Start value: {startvalue} €')
    print(f'Current value: {newvalue} €')
    startvalue = newvalue
    sleep(30)