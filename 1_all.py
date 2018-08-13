#a zadacha 2 pi r  pi d

pi= 3.14
print("ZADACHA #1")

print("Poisk po L po R kruga")
print("Vvedite R kryga")
r = input("R = ")
L1 = 2 * pi * r
print("L = %.2f" % L1)
print("Poisk po L po D kryga")
print("Vvedite D kryga")
d = input("D = ")
L2 = pi * d
print("L = %.2f" % L2)


#b zadacha  L= 2sqrt(s*pi)
print("ZADACHA #2")
import math
print("Poisk po L s ispolzovaniem MATH cherez S")
print("Vvedite S kryga")
s = input("S = ")

L = 2 * math.sqrt(s*math.pi)

print("L = 2.%f" % L)


#c zadacha korni
print("ZADACHA #3")
import math
print("Vvedite A B C dla kvadratnogo uravneina")
print("(ax^2 + bx + c = 0):")
a = input("A = ")
b = input("B = ")
c = input("C = ")

discrim = b ** 2 - 4 * a * c;
print("discrim = %.2f" % discrim)
if discrim > 0:

    x1 = (-b + math.sqrt(discrim)) / (2 * a)
    x2 = (-b - math.sqrt(discrim)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discrim == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("net kornei")