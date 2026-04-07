def stud(age,name):
    if age >=18:
        print(name, "is Eligible")
    else:
        print(name, "not eligible")

name=input("Enter the student name: ")
id=int(input("Enter the student id: "))
age=int(input("Enter the student age: "))
marks1=int(input("Enter the marks of englisgh: "))
marks2=int(input("Enter the merks of maths: "))
address=input("Enter the student address: ")

print("Name: ", name)
print("Id: ", id)
print("Address: At Post ", address)
print("Age: ", age)

stud(age,name)

total=marks1 + marks2
print("Student total marks: ", total)

total=marks1 + marks2
if total >=80:
    print("Student get Distinction")
elif total >=60:
    print("Student is Pass")
else:
    print("Student is fail")

