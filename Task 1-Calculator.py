import math

print(" This is a calculator program and takes any whole number as user input.")
while True:  #The loop runs continuously until user enters 'N' as the response.

 #These three lines of code takes the user inputs   
 num1 = input("Please enter the first number: ")
 operator = input("Please enter the operation you wish to perform(+,-,*,/): ")
 num2 = input("Please enter the second number: ")

 #The input variables are converted to float, so that result could be float i.e. along with the decimal value   
 num1 = float(num1)
 num2= float(num2)

# Depending on the parameter entered by the user the calculation is performed.    
 if operator =='+':
    result = num1 + num2
 elif operator=='-':
    result = num1 - num2
 elif operator == '*':
    result = num1*num2
 elif operator == '/':
    # If it is a division, and the denominator is entered as 0 by the user, the code runs and displays a message.
    if num2==0:
     print("Division by zero is not defined")
     continue
    else: 
     result = num1/num2
# If user enters an operator that is not valid, the code displays a message
 else:
    print("Invalid operator entered. You can choose one from +,-,*,/ for the calculations")
    continue

# This prints the final output after the calculation is complete.
 print(num1, operator, num2, '=', result)

# The loop variable is a choice of the user whether the user would like to perform another calcualtion or not
 loop = input("Do you want to perform more calculations(Y/N): ")

 if loop == 'Y':
    continue
 if loop == 'N':
    break

# This is the output if the user chooses to exit from the while loop
print("Thank you for using the calculator")






