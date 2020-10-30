This is a Python Learning Repository 
------------------------------------------
 Python
 -------
 -
    * Python was created in the late 1980's by Guido Van Rossum.
    * Python Created as a successor to 'ABC' programing Language.
    * Python is named after Guido van Rossum's favorait comedy act MONTY PYHTON
    * Python 3000 is known as the python 3.x series
    * 
-------------------------------------------------------------------------------
    
    Some python GUI Tool Kits : tkinter , wxpython , pyside , kivy

    Some web frameworks : Django , pyramid , flask
     
-------------------------------------------------------------------------------

 * " # " is used to write comments in python

 * color code in IDLE (Intergrated Devlopment and learning enviornment)  
    | functions - violet | literals - green | comment - Red | output - Blue |  

-------------------------------------------------------------------------------

 # ' Everything in python is an object '

Main datatypes in Python 
________________________

* String
* Integer
* Float
* List
* Dict
* Tuple
----------------------------------------------

Functions
----------------------------------------------
 * functions allow you to reuse functionality 
 
 syntax
 -------
        def function_Name( prameter_list ) :
           #function_body
           return varible


  * return statement and parameters list are optional
  


  
   some basic built in python funtions
   --------------------------
   * print() - used to print an object or text 
          
           print("Hello World!..") # will print 'Hello World!..' 

   * len()   - return the length of an object 

           len("Python") # will return  '6'

   * str()   - Takes an object and returns a new object as datatype 'String'

           str("123") # will return '123' as string

   * int()   - takes an object and returns a object as datatype 'int'

           int(input("value of X")) # retruns the input value as integer

   * float() - takes an object and returns a object as datatype 'float'

           float(input(enter value of X )) #returns input value as floating point value

   * input()  - capture inputs 

               a = input() # read input to a


   find more python built-in functions at : https://docs.python.org/3/library/functions.html

   ------------------------------------------------------------------------------------------------

   Exception Handling
   ---------------------------------------
   * A way to deal with exceptions when they occur
   
   Eg:
        a= int(input("type a number"))
        b= int(input("type another"))
        print(a/b)

        * this program will successfully run  if the second number(b) is not 0
        * if the second number is zero then it will cause division by zero exception

            exception handling :
              
                  try:
                    print(a/b)
                   except ZeroDivisionError:
                    print("b cannot be zero")
        