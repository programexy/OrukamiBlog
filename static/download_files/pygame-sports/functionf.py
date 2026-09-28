import time

def printf(string):
    for letter in list(string):
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print('')
def inputf(string):
    for letter in list(string):
        print(letter, end='', flush=True)
        time.sleep(0.05)
    variable = input('')
    return variable