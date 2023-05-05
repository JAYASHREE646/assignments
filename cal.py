def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("enter the option")
print("a.add")
print("b.sub")
print("c.mul")
print("d.div")
choice=input("enter the option(a/b/c/d):")
a=int(input("enter the value"))
b=int(input("enter the value"))
if choice=='a':
    print(a,"+",b,add(a,b))
elif choice=='b':
    print(a,"-",b,sub(a,b))
elif choice == 'c':
    print(a, "*", b, mul(a, b))
else:
    print(a,"/",b,div(a,b))