numbers={"1":"one",
         "2":"two",
         "3":"three",
         "4":"four",
         "5":"five"}
n=input("enter a number")
if n in numbers:
    number=numbers[n]
    print("number ",number,"is in dictionary")         
else:
    print("number not in dictionary")
