#Calculating the increase in salary
print("--The Bright Light Company employees salary increase--")

deptCode = input("Please enter deptCode: ")
anSalary = int(input("Please enter annual salary: "))

a = 0.072
b = 0.068
o = 0.063 #others

if deptCode == "a":
    increase_anSalary = anSalary + (anSalary * a)
    monSalary = increase_anSalary / 12
    print(monSalary)
elif deptCode == "b":
    increase_anSalary = anSalary + (anSalary * b)
    monSalary = increase_anSalary / 12
    print(monSalary)
elif deptCode == "o":
    increase_anSalary = anSalary + (anSalary * o)
    monSalary = increase_anSalary / 12
    print(monSalary)
else:
    print("please check the deptCode and restart")
