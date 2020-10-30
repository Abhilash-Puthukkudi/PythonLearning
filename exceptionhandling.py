#  a program that asks the user to type a number, convert it to an integer, and print it. If you can't convert their input to an integer, print a message that says "Please type an integer."

a=input("type a number ")
try:
    print(int(a))
except ValueError:
    print("sorry numbers are only allowed ")