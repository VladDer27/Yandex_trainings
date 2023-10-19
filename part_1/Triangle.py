a = int(input())
b = int(input())
c = int(input())

sum_ab = a + b
sum_ac = a + c
sum_bc = b + c

if sum_ab > c and sum_ac > b and sum_bc > a:
    print("YES")
else:
    print("NO")