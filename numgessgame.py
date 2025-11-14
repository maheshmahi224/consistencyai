import random

randomint= random.randint(1,100)
while True:
    try:
        num=int(input("enter  the  number : "))

        if randomint<num:
            print("too high")
        elif randomint>num:
            print("too low")
        elif randomint==num:
            print("congratuations you have guessed the number correctly")
            break
    except ValueError:
        print("invalid operation")
