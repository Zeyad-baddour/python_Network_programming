s = input("Write your binary number: ")
dec = 0 
if all(z in "01" for z in s):
    for i in s:
        dec = 2*dec + int(i)
    print(dec)
else:
    print("error")        