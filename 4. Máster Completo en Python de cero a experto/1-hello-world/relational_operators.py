
i, j = 3,7
k = 127e-7 # 0.000127
l = 1.1413e3 # 1141.3
m = False

b1 = i == j
print(f'b1 = {b1}')

b2 = not b1
print(f'b2 = {b2}')

b3 = i != j # <>
print(f'b3 = {b3}')

b4 = m == True
print(f'b4 = {b4}')

b5 = m != True
print(f'b5 = {b5}')

b6 = i > j
print(f'b6 = {b6}')

b7 = i < j
print(f'b7 = {b7}')

b8 = l >= k
print(f'b8 = {b8}')

b9 = l <= k
print(f'b9 = {b9}')

age = 25
b10 = age >= 10 and age <= 30
