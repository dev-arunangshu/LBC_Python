number= int(input("Enter a number: "))
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
c= int(input("Enter a number: "))


def oddEven(num):
    if num%2==0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

oddEven(number)
oddEven(a)
oddEven(b)
oddEven(c)

