from funcs import run_program

# print(startvalue)
while True:
    try:
        run_program()
    except AttributeError:
        continue
