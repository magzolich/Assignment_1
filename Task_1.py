#task 1  Implement the famous FizzBuzz algorithm!
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + " - FizzBuzz")
    elif i % 3 == 0: 
        print(str(i) +" number-that-is-divisible-by-three " +str(i)+ " - Fizz")
    elif i % 5 == 0:
        print(str(i) + " number-that-is-divisible-by-five " +str(i)+ "- Buzz")
    else:
        print(i)
