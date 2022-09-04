# if a number is Harshad
# Number or not. 
def check_Harshad( n ) :
    sum = 0
    temp = n
    while temp > 0 :
        sum = sum + temp % 10
        temp = temp // 10
    return n % sum == 0
if(check_Harshad(143)):
    print("Yes")
else:
    print ("No")

