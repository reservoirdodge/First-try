numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
skip_one = numbers[0:4]
skip_two = numbers[5:20]
Fa = (sum(skip_one)+sum(skip_two))/len(numbers)
numbers[4] = Fa
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:",numbers )
