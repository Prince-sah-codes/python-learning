def fact():
    fct = 1
    num = int(input("Enter a number: "))
    
    for i in range(num,0,-1):
       

        fct = fct * i
    print(f'Factorial of {num} is: {fct}')


fact()


