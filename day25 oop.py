# 1.	Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

import math
C=50
H=30
a = input("Enter the value of D: ").split(",")
b = []   
for D in a:
    Q = math.sqrt(2 * C * int(D) / H)
    b.append(Q)

print("Values are:", b)

# 2.         Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.

a=int(input("Enter any lenght:  "))
class Shape:
    area=0

class Square(Shape):
    def __init__(self, length):
        self.a = a

    def area(self):
        return self.a*self.a

squares= Square(a)
print ("Result:", squares.area())

# 3.          Create a class to find the three elements that sum to zero from a set of n real numbers.
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Output: [[-10,2,8],[-7,-3,10]]

class a:
 def threeSum(self, b):
        b, c, i = sorted(b), [], 0
        while i < len(b) - 2:
            j, k = i + 1, len(b) - 1
            while j < k:
                if b[i] + b[j] + b[k] < 0:
                    j += 1
                elif b[i] + b[j] + b[k] > 0:
                    k -= 1
                else:
                    c.append([b[i], b[j], b[k]])
                    j, k = j + 1, k - 1
                    while j < k and b[j] == b[j - 1]:
                        j += 1
                    while j < k and b[k] == b[k + 1]:
                        k -= 1
            i += 1
            while i < len(b) - 2 and b[i] == b[i - 1]:
                i += 1
        return c

print(a().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
 
# 4.          What is the output of the following code? Explain your answer as well.

# class Test:
#     def __init__(self):
#         self.x = 0
# class Derived_Test(Test):
#     def __init__(self):
#         self.y = 1
# def main():
#     b = Derived_Test()
#     print(b.x,b.y)
# main()

# Ans-->'Derived_Test' object has no attribute 'x'
 
# class A:
#     def __init__(self, x= 1):
#         self.x = x
# class der(A):
#     def __init__(self,y = 2):
#         super().__init__()
#         self.y = y
# def main():
#     obj = der()
#     print(obj.x, obj.y)
# main()

# Ans-->1 2
 
# class A:
#     def __init__(self,x):
#         self.x = x
#     def count(self,x):
#         self.x = self.x+1
# class B(A):
#     def __init__(self, y=0):
#         A.__init__(self, 3)
#         self.y = y
#     def count(self):
#         self.y += 1     
# def main():
#     obj = B()
#     obj.count()
#     print(obj.x, obj.y)
# main()
 
#  Ans-->3 1
 
 
# class A:
#     def __init__(self):
#         self.multiply(15)
#         print(self.i)
 
#     def multiply(self, i):
#         self.i = 4 * i;
# class B(A):
#     def __init__(self):
#         super().__init__()
 
#     def multiply(self, i):
#         self.i = 2 * i;
# obj = B()

# Ans-->30
 
# 5.	Create a Time class and initialize it with hours and minutes.
# Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Make a method displayTime which should print the time.
# Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.

class Time():

   def __init__(self, hours, mins):
     self.hours = hours
     self.mins = mins

   def addTime(self,t1, t2):
     t3 = Time(0,0)
     if t1.mins+t2.mins > 60:
      t3.hours = (t1.mins+t2.mins)//60
     t3.hours = t3.hours+t1.hours+t2.hours
     t3.mins = (t1.mins + t2.mins) % 60
     return t3

   def displayTime(self):
     print ("Time is",self.hours,"hours and",self.mins,"minutes.")

   def DisplayMinute(self):
     print ((self.hours*60)+self.mins)

a = Time(7,30)
b = Time(3,15)
c = Time.addTime(a,b)
c.displayTime()
c.DisplayMinute()


# 6.           Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:
# yearPasses() should increase the  instance variable by .
# amIOld()  should perform the following conditional actions:
# If , print You are young..
# If  and , print You are a teenager..
# Otherwise, print You are old..	
# Sample Input:
# 4
# -1
# 10
# 16
# 18
# Sample Output:
# Age is not valid, setting age to 0.
# You are young.
# You are young.
 
# You are young.
# You are a teenager.
 
# You are a teenager.
# You are old.
 
# You are old.
# You are old.

class Person:
    def __init__(self,initialAge):

        self.initialAge = age
    def amIOld(self):

        if age <= 0:
            age is 0
            print("Age is not valid, setting age to 0")

        elif age < 13:
            print("You are young.")

        elif 13 <= age < 18:
            print("You are teenager.")

        else:
            print("You are old.")
    def yearPasses(self):

        return age+1
t = int(input())
for i in range(0, t):
    age = int(input())         
    z = Person(age)  
    z.amIOld()
    for j in range(0, 3):
        z.yearPasses()       
    z.amIOld()
    print("")