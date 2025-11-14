lst=[1,2,3,4,5,6,7]
print("length of list: ",len(lst))
print("first element of the list: ",lst[0])
print("last element of the list: ",lst[-1])
lst.remove(6)
print("updated list: ",lst)
lst.reverse()
print("reverse list: ",lst)
lst=lst[1:5]
print("slice list: ",lst)