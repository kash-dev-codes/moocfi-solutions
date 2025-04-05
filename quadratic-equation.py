from math import sqrt

a = int(input('Value of a:'))
b = int(input('Value of b:'))
c = int(input('Value of c:'))

sqrtbac = sqrt((b**2) - (4 * a * c))
print(sqrtbac)

x1 = (-b + sqrtbac) / (2*a)
x2 = (-b - sqrtbac) / (2*a)

print(f'The roots are {x1} and {x2}')