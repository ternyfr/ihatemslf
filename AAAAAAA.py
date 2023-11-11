n = int(input("введите число: "))
sum = 0
x = 1
while x <= n:
    sum += x
    x += 2
print(f"сумма нечётных чисел в диапозоне от 1 до {n} равна {sum}")