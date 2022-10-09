#While and For loop
#While loops
x=0
while(x<=5):
    print(x)
    x=x+1

for x in range(5,10):
    print(x)

#Erray
days =["Mon", "Tue","Wed", "Thu","Fri","Sat","Sun"]
for d in days:
    # if (d=="Fri"):break #loop stops
    if (d=="Fri"):continue #loop skips
    print(d)