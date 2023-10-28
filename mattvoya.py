let = input("введи букву латинского алфавита\n")

gl = ["a", "e", "i", "o", "u", ]
if let.lower() in gl:
    print("введена гласная буква")
else:
    print("буква согласная")


# if let == "a" or let == "e" or let == "i" or let == "o" or let == "u":
#     print("введена гласная буква")
# elif let == "y":
#     print("эта буква может быть и гласной, и согласной")
# else:
#     print("введено некоректное значение")