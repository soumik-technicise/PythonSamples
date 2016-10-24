def addListMembers(List):
    totalSum = 0
    for i in List:
        totalSum = int(totalSum) + int(List[i-1])
 
    return totalSum
 
def multiplyListMembers(List):
    totalMultipliedAmount = 1
    for i in List:
        totalMultipliedAmount = totalMultipliedAmount * int(List[i-1])
 
    return totalMultipliedAmount
 
List1 = [1,2,3,4]
 
print ("The initial list is: " +str(List1[:]))
 
print("Sum of the members of the list is: " +str(addListMembers(List1)))
 
print("Multiplied value of the members of the list is: " +str(multiplyListMembers(List1)))
newList = List1+[5,6]
 
print("\n")
       
print ("The new list is: " +str(newList[:]))
 
print("Printing sum and multiplied value of new list")
 
print("Sum of the members of the list is: " +str(addListMembers(newList)))
 
print("Multiplied value of the members of the list is: " +str(multiplyListMembers(newList)))

 
