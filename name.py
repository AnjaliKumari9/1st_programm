Big=lambda a,b,c : a if a>b and a>c else b if b>c else c
a=int(input("a val :"))
b=int(input("b val :"))
c=int(input("c val :"))

res=Big(a,b,c)
print("Biggest one is:",res)
