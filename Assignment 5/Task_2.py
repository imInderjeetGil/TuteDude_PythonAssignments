list_1=[]
list_1.extend(range(1,11))
print("Original list:",list_1)

list_2=(list_1[0:5:])
print("Extracted firsrt five elements:",list_2)
list_2.reverse()
print("Reversed extracted elements:",list_2)