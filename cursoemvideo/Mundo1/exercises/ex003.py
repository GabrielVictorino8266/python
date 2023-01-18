#SUM TWO NUMBERS OF USER'S INPUT

n1 = int(input("What's the number 01? "))
n2 = int(input("What's the number 02? "))

sum = n1 + n2
myString = '\033[7;49;39mA soma entre {} e {} resulta é um total de {}.\033[m'

print(myString.format(n1, n2, sum))