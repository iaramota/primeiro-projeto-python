operation = input('please') type in ("the math operation you would to complete:")
     + for addition
     - for subtraction
     * for multiplication
     / for division
    

number_1 = float(input("Enter your first number: "))
number_2 = float(input("Enter your second number: "))

if opertaion == '+':
     print('{} + {} = '.format(number_1, number_2))
     print(number_1+number_2)

     if operation == '-':
          print('{} - {} = '.format(number_1, number_2))
          print(number_1-number_2)

          if operation == '*':
               print('{} * {} = '.format(number_1, number_2))
               print(number_1*number_2)
               if operation == '/':
                    print('{} / {} = '.format(number_1, number_2)
                    print(number_1 / number_2)
     

else:
     print("You have not typed a valid operator, please run the program again.")
