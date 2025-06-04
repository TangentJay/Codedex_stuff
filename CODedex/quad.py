#quadratic formula
a= int(input('bitte entre  a '))
b= int(input('bitte entre  b '))
c= int(input('bitte entre  c '))
# x= (-b + (b**2 - 4*a*c)**.5 /2*a) mine
#print(x)

r1=(-b + (b*b -4*a*c)**.5) /(2*a)
r2=(-b - (b*b -4*a*c)**.5) /(2*a) 

print(r1, r2)