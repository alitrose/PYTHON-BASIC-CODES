#INTRO
print("Hello!") 

#String methods
x = 156
y = "ALIT ROSE "
print(x)
print(y)
print(type(x))
print(y[1:5]) #slicing
print(y[-2:-3]) #slicing
print(y.replace("T","O"))#replace
print(y.split(" "))#spilt

#finding types
a,b,c="6","5","1"
print(a)
print(b)
print(c)
print(type(a))

#adding 
a = "Hello"
b = "hai"
c = a + "." + b
print(c)

#to change the frist letter in to caps
name = "alit"
o = f"My name is {name}"
print(name.capitalize())
print(o)

#reverse 
n="hello"
print(n[::-1])

#count 
n="education"
a=n.count("a")+n.count("e")+n.count("i")+n.count("o")+n.count("u")
print(a)

#Palindrome
n="madam"
if n==n[::-1]:
    print("true")
else:
    print("false")

#Capitalize
n="python is fun"
print(n.title())

#Replace
n="hello world"
print(n.replace(" ","-"))

#sum
n=[1,2,3,4]
print(sum(n))

#Maximum and Minimum
n=[5, 3, 9, 1]
a=max(n)
b=min(n)
print("max=",a)
print("min=",b )

#Remove Duplicates 
n=[1,2,2,3,4,4]



#CALCULATOR
a=int(input("enter a value="))
b=int(input("enter b value="))
r=input("select the operation(+,-,/,*)=")
if r=="+":
    print(a+b)
elif r=="-":
    print(a-b)
elif r=="*":
    print(a*b)
elif r=="/":
    print(a/b)
else:
    print("invaild")

#Logical Operators
a=int(input("enter a value="))
if a>10 and a<50:
    print("number is between 10 to 50")
else:
    print("not between 10 to 50")

#memership
if "h" in "banana":
    print("a is in banana")
else:
    print("a is not banana")



