# Better to watch Selection sort before this to understand better.

num1 = int(input("How many values do you want to input: "))
list1 = [int(input("Enter the value: ")) for x in range(num1)]
print("Unsorted list: ", list1)

for j in range(len(list1)-1): # We do len(list1)-1 bcz, A/C to the algorithm, we iterate code to swap the values, less by 1 than the length of list. Same goes to line 8.
    for i in range(len(list1)-1):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]

print("Sorted list: ", list1)

print(".....................................Next Example............................................................")

num2 = int(input("How many values do you want to input: "))
list2 = [int(input("Enter the value: ")) for x in range(num2)]
print("Unsorted list: ", list2)

for j in range(len(list2)):
    for i in range(len(list2)-1):
        if list2[i] < list2[i+1]:
            list2[i], list2[i+1] = list2[i+1], list2[i]

print("Sorted list: ", list2)
