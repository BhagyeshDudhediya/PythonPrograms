import sys
import ops

def print_menu():
    print ("1. Simple Calc. 2: Scientific Calc. 3. Exit")
    ans = raw_input("Select Calculator of your choice: ")
    return ans

ans = print_menu()
while True:
    if (ans == '1'):
        print ("1. Add 2. Subtract 3. Multiply 4. Divide 5. Go Back")
        operation = raw_input("Select operation you need to perform")
        if operation == '5':
            ans = print_menu()
            continue
        val1 = int(raw_input("Enter the first value: "))
        val2 = int(raw_input("Enter the second value: "))
        calculator = ops.Simple_Calculator(val1, val2)
        if operation == '1':
            print "Value of Addition is: " + str(calculator.add())
        if operation == '2':
            print "Value of Subtraction is: " + str(calculator.subtract())
        if operation == '3':
            print "Value of Multiplication is: " + str(calculator.multiply())
        if operation == '4':
            # An exception will be thrown if the value for val2 is 0
            try:
                print "Value of Division is: " + str(calculator.divide())
            except ZeroDivisionError:
                print "Please provide appropriate value for val2, it cannot be 0"
    elif (ans == '2'):
        print ("1. Sine 2. Cosine 3. Powerof 4. Square Root 5. Go Back")
        operation = raw_input("Select operation you need to perform")
        if operation == '5':
            ans = print_menu()
            continue
        val1 = int(raw_input("Enter the first value: "))
        val2 = 0
        if operation == '3':
            val2 = int(raw_input("Enter the second value: "))
        calculator = ops.Scientific_Calculator(val1, val2)
        if operation == '1':
            print "sin("+str(val1)+") is " + str(calculator.sine())
        if operation == '2':
            print "cosin("+str(val1)+") is " + str(calculator.cosine())
        if operation == '3':
            print str(val1)+"to the power of" + str(val2)+" is " + str(calculator.powerof())
        if operation == '4':
            print "Square root of"+str(val1)+" is " + str(calculator.square_root())
    elif (ans == '3'):
        sys.exit()
    else:
        print "Please select appropriate menu"
        ans = print_menu()

