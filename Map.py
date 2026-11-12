numbers1=(1,2,3)
numbers2=(4,5,6)
result=map(lambda x,y:x+y,numbers1,numbers2)
print("The addition of the two lists is")
print(list(result))
list1=[1,2,3,4,5]
def sq(n):
    return n*n
result_square=list(map(sq,list1))
print("The square of the numbers in the list is")
print(result_square)