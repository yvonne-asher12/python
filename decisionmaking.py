Yvonne Karimi
BSCIT-05-0072/2024
#decision making
salary=float(input("Enter your salary: "))
years_worked=int(input("Enter the years of service: "))

if (years_worked>10):
    bonus =0.1 * salary

    
elif (years_worked >=6 and years_worked <=10):
    bonus = 0.08 * salary

else :
    bonus = 0.06 * salary
    
print("The bonus is ",bonus)

f=open("C:\\Users\\User\\Desktop\\python files\\decision.txt","w")
print("The bonus is ",bonus, file=f)
f.close()
