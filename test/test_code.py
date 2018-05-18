# test for comment
print("*************")
print("test for single char operator")
print("*************")
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 % 2)
print(3 > 2)
print(3 < 2)

print("*************")
print("test for two char operator")
print("*************")
print(3 == 2)
print(3 != 2)
print(3 <= 2)
print(3 >= 2)

print("*************")
print("test for mult operator")
print("*************")
print(3 + (2 * 2))

print("*************")
print("test for string")
print("*************")
print("dyq")
print("666")

print("*************")
print("test for var")
print("*************")
a = 2 + (3 * 3)
print(a)

b = 'dyq666!!!'
print(b)

print("*************")
print("test for mult params of print")
print("*************")
print(a, b, '   ', 'aaaaa', 2)

print("*************")
print("test for log operator")
print("*************")
and1 = 3 > 2 and 3 > 1 and 3 > 0
or_test = 3 < 2 or 3 < 1
print(and1)
print(or_test)

print("*************")
print("test for if")
print("*************")
if 2 > 1: print('2>1 yes!')
if 2 < 1: print('2<1 no!')
if 2 > 1:
    print('2>1 yes!')
if 2 < 1:
    print('2<1 no!')

print("*************")
print("test for if-else")
print("*************")

a = 1 if 1 > 2 else 2
b = 2 if 1 > 2 else 1
print(a, b)

print("*************")
print("test for for")
print("*************")
for i in range(1, 5): print(i ** 2)
