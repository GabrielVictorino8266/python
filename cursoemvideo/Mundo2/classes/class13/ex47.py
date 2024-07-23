for number in range(0, 51):
    print(number, end=" ") if number % 2 == 0 else str()

print("\nManeira binaria:")

for number in range(0, 51):
    bin_representation = bin(number)
    number_size = len(bin_representation) - 1
    print(number, end=" ") if bin_representation[number_size:] == "0" else str()