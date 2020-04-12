title = "MULTIPLICATION TABLE"
print('{:^80s}'.format("\033[4m%s\033[0m"%title))
for x in range (1,13):
    for y in range(1,13):
        print ("\033[4m%4d |\033[0m" %(x*y), end = '')
    print("")
