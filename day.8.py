#day-8
#eg-3
'''
def profile(name,age,place):
   txt="my name is{}.Iam{}years old.Iam from{}."
   print(name,age,place)
profile("sneha",21,"eee")
#eg-4
#function with return statement
def f1()
    z= 8
f1()
print(z)#error-->cannot use outside the funtion
'''
'''
# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement
def f1(a,b):
    c = a*b
    return c
print(f1(6,8))
obj = f1(6,8)
obj1 = f1(4,6)
def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)
'''
'''
def ispalindrome(s):
    return s == s[::-1]
s = "333"
ans = ispalindrome(s)
if ans:
    print("yes")
else:
    print("no")
#problem-1
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("not palindrome")
a = int(input("enter the value:"))
'''
'''
#based on the declaration of parameter and args
#function are divided into 5 categories
#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
#the positoin
# * Positional args
# ? The position of parameter have to be same as position as arguments
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks{}."
    print(txt.format(name,phone,mark))
profile(96668686,"Usman",100) #unexpected
'''
'''
#keywords args
#eg-1
#to overcome the disadvantages of position args, we used keyword args
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks{}."
    print(txt.format(name,phone,mark))
profile(name="sneha",phone=566699,mark=100)#error
'''
'''
#default args
#eg-1
def profile(name,phone,place="kadapa"):
    if place!="kadapa":
       print("ypu are not eligible to signup")
    else:
     txt = "my name is {}.my phone number is {}. i am from {}."
     print(txt.format(name,phone,place))
profile("rio",354544645,"kadapa")
# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
    else:
        print("You are not eligible to Signup")
file("Shashank",9876543210)
'''
'''
#eg-1
def profile(name):
    print("my name is",name)
profile("sid",'nmae2','name3')
name = "sneha","name1","name2"
for val in name:
    print("my name is",val)
'''
'''
#eg-2
def profile(*name,age):
    for val in name:
        print("my name is",val,"may age is",age)
#profile("sneha",'name2','name3',28)#--->error

def profile(age ,*name):
    for val in name:
        print("my name is",val,"my age is",age)
profile(21,"sneha",'name2','name3')

#eg-3
#keyword variable length args
def price(**price_list):
    print(price_list)
print(shirt=1000,iphone=80000)
'''
'''
n = 5
{1:1,2:4,3:9,4:16,5:25}
n=int(input("enter the number:"))
d1 = {}
for val in range(1,n+1):
    d1[val] = val**2
print(d1)
'''
'''
def dict1(n):
    d1={}
    for val in range(1,n+1):
        d1[val] = val**2
    print(d1)
dict1(5)
#--->object orinted programming
# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation
#class is a blue print of an object
#l1 = [1,2,3,4,5,6]
#eg-1
class c1:
    name = "sneha"
print(name)
#eg-3
#creat of a method
# when the function is created of a class is called as method
class person:
    def display(person,age,name):
        print("hello welcome to classes")
p = person()
p.display()
'''
#method with parameter
class person:
    def display(person,name,age):
        print(name,age)
p = person()
p.display("sneha",21)
#eg-5
class person1:
    frame = "sai pallavi" # attribute or static variable
    lname = "s"

    def first_name(person):
        print(person.frame)

    def full_name(person):
        print(person.frame+" " +person.lname)

p = person1()
p.first_name()
p.full_name()

