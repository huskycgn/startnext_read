from funcs import get_startnext_amount, send_message, run_program

# print(startvalue)
while True:
    try:
        run_program()
    except AttributeError:
        continue
