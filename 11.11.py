# all exception are errors
# Exception handling 


try:
    a=9
    b=0
    print(a/b)
except ZeroDivisionError:
    print("error")
    
else:
    print("this code is executed")
finally:
    print("this code is successfully closed")


try:
    num1 = int(input("Enter the number: "))
    if num1 % 2 == 0:
        print("Even number")

        try:
            if num1 % 3 == 0:
                print("Also divisible by 3")
        except:
                print("Inner try failed")

except ValueError:
    print("Invalid input! Please enter a valid number.")



