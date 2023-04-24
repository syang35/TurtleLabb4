
#This code is to sort the array Ascending
length = 0 # set the array to different length or different maximum elements
length = int(input("Enter the maximum elements of the array"))
array = [0]*length
for index in range(0,length):
    array[index]= int(input("Enter the value of the element"))
remp = 0
#Sort the array
for index in range(0,length):
    for elements in range (0,length-1):
       if array[elements] > array[elements+1]:
           temp =  array[elements]
           array[elements] =  array[elements +1]
           array[elements +1] = temp
for index in range(0,length):# To print the array
    print(array[index])
