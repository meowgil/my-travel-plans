#encoding:utf-8

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

import sys

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)

# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()

def area(width, height):
    s = width * height
    return s

def print_welcome(name):
    print("Welcome", name)

print_welcome("Polyglotto")
w = 4
h = 10
print("width = ", w, " height = ", h, " area = ", area(w, h))

def printme( str ):
    print (str)
    return

printme(u"哈哈哈嗝哈哈哈嗝哈哈哈嗝")
printme(u"红红火火恍恍惚惚")  #运行没问题，打不出字


def printinfo( name, age = 5):
    print ("name: ", name)
    print ("age: ", age)
    return

printinfo( age = 50,name = "hhh")
print ("----------------------------------------------")
printinfo(name = "hhh")


def printparameter(arg1, *vartuple):
    print ("output: ")
    print (arg1)
    print (vartuple)

printparameter( 70, 60, 50)

def printinfo( arg1, **vardict ):
    print ("output: ")
    print (arg1)
    print (vardict)

printinfo(1,a=2,b=3)


sum = lambda arg1, arg2: arg1 + arg2

print ("sum: ", sum( 10, 20))
print ("sum: ", sum( 20, 20))

product = lambda num1, num2: num1*num2

print ("prodct: ",product(10,10))

def sum( arg1,arg2):
    total = arg1+arg2
    print ("in function:", total)
    return total

total = sum(10 ,20)
print ("off function: ", total)

total = 0
def sum(arg1, arg2):
    total = arg1 + arg2
    print ("in function is pvar: ",total)
    return total

sum( 10, 20)
print ("off function is avar: ",total)

num = 1
def fun1():
    global num
    print(num)
    num = 123
    print (num)

fun1()
print(num)

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)
outer()

s = 10
def test(s):
    s +=1
    print(s)    
test(s)