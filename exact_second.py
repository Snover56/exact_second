# Written by Matthew Quinn
# Last updated: 6/9/20

import time

def round(x):
    if float(x) != int(x) and float(str(x)[str(x).index('.') + 1]) >= 5:
        if x > 0:
            return int(x) + 1
        elif x < 0:
            return int(x) - 1
    return int(x)

print('In this game, you will try and approximate exactly one second as best you can.')
input('Press enter to begin.')
while(True):
    input('>>> ')
    starttime = time.monotonic()
    input('>>> ')
    endtime = time.monotonic()
    elapsed = endtime - starttime
    error = (elapsed - 1) * 100
    if error < 0:
        error = error * -1
    error = round(error)
    if elapsed < 10:
        elapsed = str(elapsed)[0:5]
    else:
        elapsed = str(elapsed)[0:6]
    print(elapsed + ' seconds.')
    print(str(error) + '% error.')
    if error == 0:
        print("You win! Congrats")
