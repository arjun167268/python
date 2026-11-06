str=input("enter the string:")
if len(str)<=1:
    print("string 10 to small")
else:
    new=str[-1]+str[1:-1]+str[0]
    print(new)
                           
