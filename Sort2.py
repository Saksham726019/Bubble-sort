# Here, we will see the iterated output as well.

num1 = int(input("How many values do you want to input: "))
list1 = [int(input("Enter the values: ")) for x in range(num1)]
print("Unsorted list: ", list1)

for j in range(len(list1)):
    for i in range(len(list1)-1-j): # We do '-j' so that there won't be comparison between the values which is already compared and swapped.
        if list1[i] > list1[i + 1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
            print(list1)
        else: # We use else:, so that it will print all the steps. If not used, then only the steps where values are swapped, will be printed.
            print(list1)
    print() # This is to create a space after each part of iteration.

print("Sorted list: ", list1)

print(".....................................Next Example............................................................")

num2 = int(input("How many values do you want to input: "))
list2 = [int(input("Enter the value: ")) for x in range(num2)]
print("Unsorted list: ", list2)

for j in range(len(list2)-1):
    for i in range(len(list2)-1-j):
        if list2[i] < list2[i+1]:
            list2[i], list2[i+1] = list2[i+1], list2[i]
            print(list2)
        else:
            print(list2)
    print()

print("Sorted list: ", list2)

