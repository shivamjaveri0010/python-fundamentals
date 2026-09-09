dividend = (int)(input())
divisor = (int)(input())

if (divisor <= 0):
    print("This is invalid!")
    
remainder = dividend % divisor
print(f"The remainder when {dividend} is divided by {divisor} is: {remainder}")