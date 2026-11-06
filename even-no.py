list=list(map(int,input("Enter the list of numbers:").split()))
for num in list:
    if num%2==0:
        list.remove(num)
print("list after removal is :",list)
