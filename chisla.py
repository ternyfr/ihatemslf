# chi = int(input("введи натуральное число:"))
# deli = 0

# if chi < 0:
#     print("натуральное число надо.")
# elif chi == 1:
#     print("1 это ни простое ни составное")
# elif chi > 1:
#     for i in range(2, chi // 2):
#         if chi % i == 0:
#             deli = deli + 1
#     if deli == 0:
#         print("число простое")
#     else:
#         print("число составное")

num = 14
de = 0
for i in range(2, num):
    if (num % i == 0):
        de = de+1
if de>0:
    print(f"число {num} составное")
else:
    print(f"число {num} простое")