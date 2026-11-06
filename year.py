current_year=int(input("Enter the current year: "))
final_year=int(input("Enter the final year: "))
for i in range(current_year,final_year + 1):
 if(i%400==0)or(i%4==0 and i%100!=0):
  print(i)
