
print("Please enter a number:")
inputNumber = input()
inputLength = len(inputNumber)
numberList = []

for x in range (inputLength):
   numberList.append(int(inputNumber[x]))

print(numberList)
