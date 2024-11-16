#The radius of circle is 45cm, if pie =3.142. ,Write a python code that will calculate the area of the circle and the circumference of the circle. 
# Add the area and the circumference together and print tit out
r=45
p=3.142
area=p*r*r
print(area)
c=2*p*r
print(c)
sum=area+c
print(sum)
if sum>50:
    print("a messsge its greater")
    total=sum*100
    print(total)
else:
    print("a message it is less than")
    total=sum+1000
    print(sum)