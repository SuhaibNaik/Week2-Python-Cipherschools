#data structures 
#list
a=[1,2,"hello",'four',2.3]
print(a)
print(a[3])    #you can access list items via indexing and slicing 

#list methods
fruits=['grapes','apple','grapes']
fruits.append('mango')  #adds data at last of list
fruits.insert(1,'orange')  #will add data at index 1
veg=['potato','spinach','cabbage']
print(fruits+veg)
fruits.extend(veg)   #adds data of list veg to list fruits
fruits.append(veg)   #adds list veg inside list fruits

fruits1=['grapes','apple','grapes','orange','banana','mango']
#pop method
fruits1.pop(1) #delete element of index 1
del fruits1[4]  #delete element of index 4
fruits.remove('grapes') #removes grapes from list

numbers=[1,2,3,1,4,5,6,8,9]
print(numbers.count(1))  # counts how many times an element is present
print(sorted(numbers))   # prints list in sorted way but doesnt change original list
numbers.sort()   #sorts the elements in ascending order
#numbers.clear()  #deletes all items in list
numbers_copy=numbers.copy() #makes copy of original list

#split method
info='suhaib 18'.split()    #splits string where sapce is present
print(info)   #creates a list ['suhaib','18'] 
a=input().split(',')    #takes inputs separated by comma
b=['suhaib', '19']
print(''.join(b))    #joins elements of list 

#list inside list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][1])   #will print first element from ist list inside main list

nums=list(range(0,11))   #will give list from 0 to 11

#min and max
a=[2,8,4,5]
print(max(a))
print(min(a))