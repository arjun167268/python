str=input("Enter a string:")
if len(str)<3:
    print(str)
elif str.endswith("ing"):
    print(str+"/ly")
else:
    print(str+"ing")
