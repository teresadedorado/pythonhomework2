gross_salary =input("What is your gross salary? ")
nchildren = input("How many children do you have? ")

try:
    gross_salary= int(gross_salary)
    nchildren= int(nchildren)

except ValueError:
    print("numbers are invalid")
    exit (1)

if gross_salary < 1000:
    net_salary = (0.9+(nchildren*0.01))*gross_salary
    print("Your net salary is", round(net_salary), "euros")
elif 1000 <= gross_salary <2000:
    net_salary = (0.88+(nchildren*0.01))*gross_salary
    print("Your net salary is", round(net_salary), "euros")
elif 2000 <= gross_salary <4000:
    net_salary = (0.86+(nchildren*0.005))*gross_salary
    print("Your net salary is", round(net_salary), "euros")
else:
    net_salary = (0.82 + (nchildren * 0.005))*gross_salary
    print("Your net salary is", round(net_salary), "euros")


