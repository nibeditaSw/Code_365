# Designer Door Mat

a=9
b=27
s1=".|."
s2="WELCOME"

for i in range(a//2):
   print((s1*((i*2)+1)).center(b,"-"))

x = s2.center(b,"-")
print(x)

for i in range(a//2-1,-1,-1):
   print((s1*((i*2)+1)).center(b,"-"))
