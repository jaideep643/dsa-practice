def max_min_of_two_numbers():
    a,b= map(int,input("enter two numbers seperated by space:").split())
    if a>b:
        print("the max is:",a)
    else:
        print("the max is:",b)

max_min_of_two_numbers()