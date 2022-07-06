"""
Description:
This is a simple Python script which 
finds the exact mid-night time-point, 
given the starting and ending time of 
the night
"""


start = input("Enter night starting time (HH:MM) [will be taken as PM] - ")
end = input("Enter night ending time (HH:MM) [will be taken as AM - ")

a,b = start.split(':')
e,f = end.split(':')

a,b,e,f = int(a), int(b), int(e), int(f)

c = int(a)*60
d= c+ b
g = e*60 + 60*12
h = g + f
i = h- d
j = i/2
k= j//60
l= j - k*60
m= a+k

if m>12:
 z= m - 12
 n= b + l
 if n>60:
   o = n -60
   p = z+1
   print(p, ":", o)
 else:
  print(z, ":", n)
elif m<= 12:
  n= b + l
  if n>60:
   o = n -60
   p = m+1
   print(p, ":", o)
  else:
   print(m, ":", n)


   