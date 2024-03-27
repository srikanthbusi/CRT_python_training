# n = input().split()
# list1 = [int(unq) for unq in n]
# list2= []
# for unq1 in list1:
#     if unq1 not in list2:
#         list2.append(unq1)
# print(list2)


# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_elements = []
# for element in my_list:
#     if element not in unique_elements:
#         unique_elements.append(element)
# print(unique_elements)  # Outputs: [1, 2, 3, 4, 5]
n = input().split()
common = [int(unq) for unq in n]
unique =[]
for i in common:
    if i not in unique:
        unique.append(i)
print(unique)