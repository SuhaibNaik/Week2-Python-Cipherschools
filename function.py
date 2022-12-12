#function
def add():         #without any parametes
    print(5+10)
add()
def add_nums(a,b):     #parameters are used
    print(a+b)
add_nums(7,10)   #arguement is passed
#or we can use return 
#example
def sub(a,b):
    return a-b
x=int(input())
y=int(input())    #parameters and arguement used
print(sub(x,y))     #we need to print the function if we use return function

#example
def odd_even(num):
    if num%2==0:
        return "even"
    return "odd"
a=int(input())
print(odd_even(a))
#example2
def is_even(number):
    return number%2==0
print(is_even(10))
#example 3    print greatest number
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greatest(10,40,15))


#example 5 whether palindrom or not
def is_palindrom(word):
    return word==word[::-1]
str1=input()
is_palindrom(str1)