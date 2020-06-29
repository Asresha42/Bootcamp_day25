# Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.

def division(m):
    return True if m % 3!= 0 and m%7==0 else False
print(division(23))
print(division(35))

# Write a program in Python to multiple the element of list by itself using a traditional function and pass the function to map to complete the operation.

def b(c):
    return c * c
a=[89,90,5,7,333,45,6,11,22,456]
print(list(map(b,a))) 

# Write a program to Python find out the character in a string which is uppercase using list comprehension.

a="AsrESha KaR"
b=[c for c in a if c.isupper()]
print(b)

# Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
# ● Student = [&#39;Smit&#39;, &#39;Jaya&#39;, &#39;Rayyan&#39;]
# ● capital = [&#39;CSE&#39;, &#39;Networking&#39;, &#39;Operating System&#39;]


students = ["Smit", "Jaya", "Rayyan"] 
capital = ["CSE","Networking", "Operating System"]
print ("Students : " + str(students)) 
print ("Capital : " + str(capital)) 
a = dict(zip(students, capital)) 
print ("Information : " +  str(a))


# Learn More about Yield, next and Generators
# Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

def a(b):
    for i in range (len(b) - 1, -1, -1):
        yield b[i]
for i in a('Consultadd Training'):
    print(i ,end="")

# Write any example on decorators.

def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello())

# Write a program to handle an error if the user entered the number more than four digits it should return “Please length is too short/long !!! Please provide only four digits

while True:
    a = input("Enter the numbers: ")
    if len(a)==4:
        print(a)
        break
    else:
        print("Please length is too short/long !!! Please provide only four digits")

# Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.

i = 0
while (i<3):
    a = str(input("Enter Email Id: "))
    b = str(input("Enter password: "))
    if a=="asha5@gmail.com" and b =="asha":
        print("Welcome!")
        break
    else:
        print("Retry wrong values")
        i+=1

        
     




