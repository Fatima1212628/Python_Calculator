import math

class Base:

  def display_functions(self):
    data=input(" Calculator (on/off) : ").lower()

    if data =='on':
     
     print("----Scientific Calculator----")
     print("+: Addition")
     print("-: Subtraction")
     print("*: Multiplication")
     print("/: Division")
     print("s: Square")
     print("sqr: Square Root")
     print("cu: Cube")
     print("cr: Cube Root")
     print("p: Power")
     print("n: Sine (radians)")
     print("c: Cosine (radians)")
     print("t: Tangent (radians)")
     print("l: Logarithm (base 10)")
     print("al: Antilogarithm (base 10)")
     print("g: Percentage")
     print("e: Exit")

     choice=input("Enter your choice : ").lower()
     print()
     return choice
    
    else:
      return 'e' # Return 'e' to signal program exit in the main loop
    

class Calculator(Base):
  def __init__(self):
    pass
  
history=[] # stores calculators history
while  True:
  object=Calculator()
  choice=object.display_functions() # variable made that gets user's menus choice
  
  if choice == 'e':
    break

  if choice =='+':
    num1=int(input("Enter number 1 :"))
    num2=int(input("Enter number 2 :"))
    result=num1+num2
    history.append(f"{num1} + {num2} = {result}")
    print(f"{num1} + {num2} = ",result)
    print()
    

  elif choice =='-':
    num1=int(input("Enter number 1 :"))
    num2=int(input("Enter number 2 :"))
    result=num1-num2
    history.append(f"{num1} - {num2} = {result}")
    print(f"{num1} - {num2} = ",result)
    print()

  elif choice =='*':
    num1=int(input("Enter number 1 :"))
    num2=int(input("Enter number 2 :"))
    result=num1*num2
    history.append(f"{num1} * {num2} = {result}")
    print(f"{num1} * {num2} = ",result)
    print()
  
  elif choice =='/':
    num1=int(input("Enter number 1 :"))
    num2=int(input("Enter number 2 :"))
    if num2==0:
      print("Error.Cannot divide by zero")
      continue # to exit and start again
    result=num1/num2
    history.append(f"{num1} / {num2} = {result}")
    print(f"{num1} / {num2} = ",result)
    print()

  elif choice =='s':
    num1=int(input("Enter number :"))
    result=num1**2
    history.append(f" Square of {num1} = {result}")
    print(f"Square of {num1} = ",result)
    print()

  elif choice =='sqr':
    num1=int(input("Enter number :"))
    if num1 < 0:
       print("Error: Square root of negative number is not real\n")
       continue
    result=math.sqrt(num1) # import math library for working of square root , cube roots 
    history.append(f"Square root of {num1} = {result}")
    print(f"Square root of {num1} = ",result)
    print() 

  elif choice =='cu':
    num1=int(input("Enter number :"))
    result=pow(num1,3)
    history.append(f"Cube of {num1} = {result}")
    print(f"Cube of {num1} = ",result) 
    print()

  

  elif choice =='cr':
    num1=int(input("Enter number :"))
    result=math.cbrt(num1)
    history.append(f"Cube root of {num1} = {result}")
    print(f"Cube root of {num1} = ",result)   
    print()  

  elif choice =='p':
    num1=int(input("Enter base number :"))
    num2=int(input("Enter exponent number : "))
    result=pow(num1,num2)
    history.append(f"{num1} ^ {num2} = {result}")
    print(f"{num1} ^ {num2} = ",result)
    print()

  elif choice =='n':
    num1=float(input("Enter angle in radian :"))
    result=math.sin(num1)
    history.append(f"Sineθ  {num1} = {result}")
    print(f"Sineθ  {num1} = ",result) 
    print()

  elif choice =='c':
    num1=float(input("Enter angle in radian :"))
    result=math.cos(num1)
    history.append(f"Cosθ  {num1} = {result}")
    print(f"Cosθ  {num1} = ",result) 
    print()

  elif choice =='t':
    num1=float(input("Enter angle in radian :"))
    result=math.tan(num1)
    history.append(f"Tangentθ {num1} = {result}")
    print(f"Tangentθ {num1} = ",result)  
    print()

  elif choice =='l':
    num1=int(input("Enter number :"))
    if num1 <= 0:
      print("Error: Logarithm is only defined for positive numbers\n")
      continue
    result=math.log10(num1)
    history.append(f"Log10 {num1} = {result}")
    print(f"Log10 {num1} = ",result) 
    print() 

  elif choice =='al':
    num1=float(input("Enter number :"))
    result=10**num1
    history.append(f"Antilog10 ({num1}) = {result}")
    print(f"Antilog10 ({num1}) = ",result) 
    print() 



  elif choice =='g':
    num1=float(input("Enter number 1 :"))
    num2=float(input("Enter number 2 : "))
    if num2 == 0:
      print("Error: Whole cannot be zero")
      continue
    result=(num1/num2)*100
    history.append(f"{num1} / {num2} * 100 = {result}")
    print(f"{num1} / {num2} * 100 = ",result) 
    print() 

  else:
    print("Invalid Choice.\n Please enter correct choice.") 
  
  permission=input("Want to view Calculator's history (yes/no):").lower()
  if permission =='yes':

   print("Calculator History:", history)  
   print()








    


  
  


