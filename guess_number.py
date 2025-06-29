'''
#######   Welcome to guess_number2   #######
1. Random number will be genrated
2. User will get 10 chance to guess number
3. Afert every guess system will give hint by saying guess is greater to lower then number

'''

import random

def n_dif_num(n):
    '''
    1. Return n th digit non repitive number
    2. Return string not integer  
    '''
    num=f'{random.randint(1,9)}'
    for i in range(n-1):
        
        while True:
            test=str(random.randint(0,9))
            if not test in num:
                num += test
                break
    return num

num=int(n_dif_num(4))

for i in range(15):
    print(i+1,'.')
    user=int(input("Enter any 4 digit number: "))
    if user==num:
        print(f"Congratulation {user} is correct answer")
        break
    elif user<num:
        print("Input number is less than orignal number")
    else :
        print("Input number is greater than orignal number")
    print("\n")        
            
        

