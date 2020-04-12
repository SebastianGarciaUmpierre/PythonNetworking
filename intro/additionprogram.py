inputNumber =int(input ("Choose a number: "))+1
currentTotal = 0

for x in range (1,inputNumber):
    if 0 == (x%3) or 0 == (x%5):
        currentTotal += x
        if ( x < (inputNumber - 1)):
            print ("%d + " %x, end = ' ')
        else:
            print ("%d = %d" %(x, currentTotal))
