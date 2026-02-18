
def fact(num):
    
    if num == 1:
        return 1 
    else:
        factorial = num * fact(num-1)
        return factorial 

print(f' Factorial  is {fact(4)}')       



