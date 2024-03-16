#task 3 Implement Greatest Common Divisor (GCD or in Polish Największy Wspólny Podzielnik) algorithm.
a = int(input("Provide a first number: "))
b = int(input("Provide a second number: "))
if a == b:
    print(a)
else:
    while a != b:
        if a>b:
            a = a-b            
        elif a<b:
            b = b-a               
    print(a)