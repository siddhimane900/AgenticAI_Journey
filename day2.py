def wel(name):
    print("hello", name)
wel("Guy's")
wel("Siddhi")
wel("omkar")

def add_numbers(a, b):
    print("Sum: ", a+b)
def sub_numbers(a, b):
    print("Sub: ", a-b)
def mult_numbers(a, b):
    print("Multiplication: ", a*b)
def div_numbers(a, b):
    print("Division: ", a/b)
add_numbers(2, 5)
add_numbers(4, 69)
add_numbers(14, 9)
add_numbers(54, 32)
sub_numbers(33,2)
sub_numbers(102,54)
mult_numbers(12,9)
mult_numbers(0,12)
div_numbers(9,3)
div_numbers(100,3)
def check_eiligibility(name, age):
    if age >=18:
        print(name,"is Eligible")
    else:
        print(name,"is not Eligible")
for i in range (4):
    name=input("Enter the Name")
    age=int(input("Enter the Age"))
    check_eiligibility(name, age)
