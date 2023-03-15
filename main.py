from funcs import get_startnext_amount, send_message
from time import sleep

startvalue = get_startnext_amount()
print(startvalue)
while True:
    newvalue = get_startnext_amount()
    if newvalue != startvalue:
        send_message(f'Betrag ist jetzt {newvalue} €')
    sleep(30)