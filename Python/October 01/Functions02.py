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
"""
#5.GreetingFunction
def greeting(name):
    return name
x = greeting(" Kai")
print(f"Hello,{x}")

#6. Find the Cube
def cube(a):
    return a**3
y = cube