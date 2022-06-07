my_list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input()) 
    my_list.append(ele)   
my_list.sort()
print("The list after sorting is :")
print(my_list)