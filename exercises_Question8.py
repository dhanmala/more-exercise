list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
new_list=[]
for i in list1:
    if i not in list2:
        list2.append(i)     
        list2.sort()     
print(list2)
