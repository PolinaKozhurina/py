numbers = input("Put 10 numbers in a row: \n").split() #сканирует всю строку и разделяет ее в случае нахождения разделителя
numbers = list(map(int, numbers))
n = 0
for i in range(len(numbers) - 1):
    if numbers[i+1] < numbers[i]: 
        n += 1
print(numbers)
if n == 0:
    print("Numbers are sorted in ascending order.")
else:
    print("Numbers are not sorted in ascending order.")