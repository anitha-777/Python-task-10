# 1. Print All Duplicate Characters in a String
s="aabacdegebd"
r=""
n=""
for i in s:
    if i not in n:
        n+=i
    else:
        r+=i
print(r)

# 2. Replace Vowels with ‘*’

s="python Developer"
x=""
for i in s:
    if i in "AEIOUaeiou":
        x+='*'
    else:
        x+=i

print(x)



# 3. Convert a Snake_Case String to CamelCase.
x="hello_world"      #snake_case
y=x.split("_")
z=""
for i in range(len(y)):
     if i>=1:
          z+=y[i].capitalize()
     else:
          z+=y[i]
print(z)            #camelCase


# 4. Use reduce() to Find Product of List Elements

from functools import reduce 
l=[12,10,20,30]
res=reduce(lambda a,b:a*b,l)
print(res) 