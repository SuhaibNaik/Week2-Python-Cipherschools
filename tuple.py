#tuple dat structure 
#tuple can store any data
#tuples are immutable
#tuple methods
# count,index,len<slicing
a=(1,2,3,4,5)  
fruits='orange','mango','apple'  #tuple without  paranthesis


#list insiede tuple
v=(1,2,3,4,[2,6,8,9,0])
v[1].pop()            # we can change data of list inside tuple
v[1].append(0)   


#min and max as used in list
print(min(a))
print(max(a))
#sum
print(sum(a))