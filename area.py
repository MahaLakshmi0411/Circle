pi=3.14
r=float(input("Enter the radius of a circle:"))
area=pi*r*r
print("The area of the circle is =%.2f"%area)
i = input("Input the Filename: ")
extns =i.split(".")
print ("The extension of the file is : " + repr(extns[-1]))
