l1=[1,3,4,2,5]
l2=[3,4,5,2,3,8]
print(l1)
print(l2)
print("Nested List:")
l3=[l1,l2]
print(l3)
print("Length")
print("Length of l1:",len(l1))
print("Length of l2:",len(l2))
print("Concatenation")
print(l1+l2)
print("Membership:")
print("To check a given element in the list")
ch=int(input("Enter a number to check:"))
if ch in l1:
    print("Present.")

else:

    print("Not present.")

print("Iteration:")

print("To ierate through l2:")

for i in l2:

    print(i,end=" ")

print()

print("Indexing")

print(l1[2])

print("Slicing")


print(l2[1:4])
