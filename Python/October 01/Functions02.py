"""#1. add two no,
def add(a,b,c):
    return a+b+c
result=add(10,20,30)
print(result)

#2.check odd vs even:
def check_no(no):
    if no%2==0:
        return "Even"
    else:
        return "Odd"
print(check_no(10))
print(check_no(13))
print(check_no(12))


#3.find square of each no:
def sq(no):
    return no**2
x = sq(11)
y = sq(17)
print(x)
print(y)

#4.find maximum
def max(a,b):
    if a>b:
        return a
    if a<b:
        return b
    else:
        return "both are equal"
res = max(100,66)
ret = max(100,166)
ren = max(100,100)
rem = max(-1090,-100)
print(res)
print(ret)
print(ren)
print(rem)

#5.GreetingFunction
def greeting(name):
    return name
x = greeting(" Kai")
print(f"Hello,{x}")

#6. Find the Cube
def cube(a):
    return a**3
y = cube(9)

#7. Check Positive, Negative, or Zero
def no(a):
    if a>0:
        print(f"positive,{a}")
        return a   # always use return at last after everything it will exit the loop.
       
    if a<0:
        print(f"Negative,{a}")
        return a
        
    else:
        print("Zero")
        return a 
        
res=no(6)
res=no(-2)
res=no(0)
print(y)

#8. Calculate the Average of Three Numbers
def no(a,b,c):
    return (a+b+c)/3
x = no(10,2,45)
y = no(345,3443,34)
print(x)
print(y)

#9. Calculate Factorial
def no(a):
    x = 1
    for i in range(1,a+1):
         x = x*i
    return x
print(no(5))

#10. Sum of List Elements
def no(c):
    x=0
    for i in c:
        x += i
    return x
y = [100,22,33,43,332,32212,22]
print(no(y))

"""
#.1 Find All Prime Numbers in a List
def no(d):
    x = 2
    for i in d:
        i % x != 0
        x = i
        