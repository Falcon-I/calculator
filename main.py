while True:
    try:
        x = int(input("Enter the first number : "))
        y = int(input("Enter the second number : "))
        function = input("Enter the function (+ or - or * or /) : ")
        if function == '+':
            print(x+y)
        elif function == '-':
            print(x-y)
        elif function == '*':
            print(x*y)
        elif function == '/':
            print(x/y)
        else:
            print("Something went wrong")
    except:
        print("Something went wrong")
