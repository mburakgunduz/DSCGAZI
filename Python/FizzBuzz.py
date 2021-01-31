x = int(input("Birinci sayıyı giriniz" ))
y = int(input("İkinci sayıyı giriniz" ))

for x in range(x,y): 
    if x % 3 == 0:
        if x % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)