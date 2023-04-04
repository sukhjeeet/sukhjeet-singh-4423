a = int(input ("enter month"))
b = int(input ("enter date"))
c = int(input ("enter year"))
d=1

if a >0 and a <=12:
    d = 1
else:
    d=0


if b >0 and b <=31:
    d = 1
else:
    d=0
    
if c >0 and c <=99:
    d = 1
else:
    d=0

if d == 0:
    print("invalid")
else:
    print("Success: Congratulations! you entered the correct date.")
    print("the date is",a,"/",b,"/",c)
    



    