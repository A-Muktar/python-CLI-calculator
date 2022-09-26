print("\n\t", '\\'*55, "\n\t\tWelcome to new Python Command line Calculater\n\n\t\t","**"*4, "Design by TechLead Co. LTD", "**"*4,"\n\t",'\\'*55, "\n" )

num1 = int(input("Enter first number: ")) #to accept first value
operators = input("Enter the sign to use (e.g + _ * /): ") #to accept the arithmetic sign
num2 = int(input("Enter second number: ")) #to accept second value
  
  #for addition
if operators== "+":
    print("The answer is: ", num1+num2)
    # for subtraction
elif operators == "-":
        print("The answer is: ", num1-num2)
        #for multiplication
elif operators =="*":
        print("The answer is: ", num1*num2)
        #for division
elif operators == "/":
        print("The answer is: ", num1//num2)
        #fallback, incase the user want to use other arithmetic signs that is not included
else:
    print("The arithmethic sign you enter is invalid")
    # asking the user to close the program
    input("\tPress enter to quit the program...")



    
