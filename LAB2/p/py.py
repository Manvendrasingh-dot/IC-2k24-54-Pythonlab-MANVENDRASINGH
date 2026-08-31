# print("manvendra is a bevkoof insan")
# a=int(input("enter the number:"))
# if a%2==0:
#     print("even number")
# else:
#     print("odd number")

# write  PYTHON SCRIPT TO IDENTIFY GREATEST OF 3 USER DEFINED INTEGERS 
A,B,C=input("enter the three numbers").split()
# print(A,B,C)
if A>B and A>C:
    print(A,"is the greatest number")
elif B>A and B>C:
    print(B,"is the greatest number")
else:
    print(C,"is the greatest number")