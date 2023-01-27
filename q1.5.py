#program to reverse a string
str=input("Enter the desired string:")
rev_str=" "
for i in str:
    rev_str=i+rev_str
print("The reversed string is:",rev_str)