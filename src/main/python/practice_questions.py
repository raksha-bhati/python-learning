###################
# interchange first and last element of list
###################
input = [1,2,3,4,5,6,7,8,9,10]
print(input)
input[0] , input[-1] = input[-1] , input[0]
output = input
print(output)

###################
# interchage elements of list with given positions to be changed , Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
###################
input_list = [23,65,19,90]
print("input string is : ",input_list)

def swapPositions(lis, pos1, pos2):
    lis[pos1], lis[pos2] = lis[pos2], lis[pos1]
    return lis

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
List1=[1,2,3,4,5]
print(swapPositions(List, pos1 - 1, pos2 - 1))
print(swapPositions(List1, pos1 - 1, pos2 - 0 ))

###################
# find length if a list
###################
input = [10,20,30,40,50,60,70,80,90,100]
print("lenght if the list is :  " , len(input))

###################
# chekc if element is present in  list
###################
input = [10,20,30,40,50,60,70,80,90,100]
element = 52
'''time complexity is O(1)'''
if element in input:
    print(element , " is present in list")
else:
    print(element , " is not present in list")


###################
#
###################